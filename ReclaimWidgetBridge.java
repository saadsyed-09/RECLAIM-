package com.reclaim.app;
import android.appwidget.AppWidgetManager;
import android.content.ComponentName;
import android.content.Context;
import android.app.Activity;
import android.webkit.JavascriptInterface;
import org.json.JSONObject;
public class ReclaimWidgetBridge {
 private final Context context; private final Activity activity;
 public ReclaimWidgetBridge(Activity a){activity=a;context=a.getApplicationContext();}
 @JavascriptInterface public String getLaunchPage(){String p=activity.getIntent().getStringExtra("reclaim_page");return p==null?"":p;}
 @JavascriptInterface public void updateWidgetData(String json){try{JSONObject d=new JSONObject(json);context.getSharedPreferences("reclaim_widget_data",0).edit().putInt("xp",d.optInt("xp",0)).putInt("level",d.optInt("level",1)).putInt("levelProgress",d.optInt("levelProgress",0)).putString("levelName",d.optString("levelName","LEVEL")).putInt("streak",d.optInt("streak",0)).putInt("doneCount",d.optInt("doneCount",0)).putInt("totalMissions",d.optInt("totalMissions",3)).apply();ReclaimWidgets.updateAll(context);}catch(Exception ignored){}}
}
