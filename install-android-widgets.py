#!/usr/bin/env python3
import os, shutil
app='android/app/src/main'; src='android-widget'
java_dst=os.path.join(app,'java','com','reclaim','app');os.makedirs(java_dst,exist_ok=True)
for f in os.listdir(os.path.join(src,'java','com','reclaim','app')):shutil.copy2(os.path.join(src,'java','com','reclaim','app',f),os.path.join(java_dst,f))
for sub in ('layout','xml'):
 dst=os.path.join(app,'res',sub);os.makedirs(dst,exist_ok=True)
 for f in os.listdir(os.path.join(src,'res',sub)):shutil.copy2(os.path.join(src,'res',sub,f),os.path.join(dst,f))
manifest=os.path.join(app,'AndroidManifest.xml'); text=open(manifest,encoding='utf-8').read()
receivers=("\n<receiver android:name=\".ReclaimXpWidget\" android:exported=\"true\"><intent-filter><action android:name=\"android.appwidget.action.APPWIDGET_UPDATE\" /></intent-filter><meta-data android:name=\"android.appwidget.provider\" android:resource=\"@xml/reclaim_widget_xp\" /></receiver>\n"
"<receiver android:name=\".ReclaimStreakWidget\" android:exported=\"true\"><intent-filter><action android:name=\"android.appwidget.action.APPWIDGET_UPDATE\" /></intent-filter><meta-data android:name=\"android.appwidget.provider\" android:resource=\"@xml/reclaim_widget_streak\" /></receiver>\n"
"<receiver android:name=\".ReclaimMissionsWidget\" android:exported=\"true\"><intent-filter><action android:name=\"android.appwidget.action.APPWIDGET_UPDATE\" /></intent-filter><meta-data android:name=\"android.appwidget.provider\" android:resource=\"@xml/reclaim_widget_missions\" /></receiver>\n")
if '.ReclaimXpWidget' not in text:text=text.replace('</application>',receivers+'</application>')
open(manifest,'w',encoding='utf-8').write(text)
main=None
for dp,_,fs in os.walk(os.path.join(app,'java')):
 for f in fs:
  if f=='MainActivity.java':main=os.path.join(dp,f);break
 if main:break
if not main:raise SystemExit('MainActivity.java not found in generated Android project')
s=open(main,encoding='utf-8').read()
if 'ReclaimWidgetBridge' not in s:
 s=s.replace('import com.getcapacitor.BridgeActivity;','import com.getcapacitor.BridgeActivity;\nimport com.reclaim.app.ReclaimWidgetBridge;\nimport android.content.Intent;')
 s=s.replace('super.onCreate(savedInstanceState);','super.onCreate(savedInstanceState);\n        bridge.getWebView().addJavascriptInterface(new ReclaimWidgetBridge(this), "ReclaimWidgetBridge");')
 if 'onNewIntent(Intent intent)' not in s:
  body='''
    @Override
    public void onNewIntent(Intent intent) {
        super.onNewIntent(intent);
        setIntent(intent);
        String page=intent.getStringExtra("reclaim_page");
        if(page!=null && bridge!=null && bridge.getWebView()!=null){
            final String safePage=page.matches("[a-z]+")?page:"home";
            bridge.getWebView().post(() -> bridge.getWebView().evaluateJavascript("window.reclaimOpenWidgetPage && window.reclaimOpenWidgetPage('" + safePage + "')", null));
        }
    }
'''
  before, closing = s.rsplit('\n}',1)
  s=before+body+'\n}'+closing
 open(main,'w',encoding='utf-8').write(s)