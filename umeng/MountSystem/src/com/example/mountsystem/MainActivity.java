package com.example.mountsystem;

import java.io.DataOutputStream;
import java.io.IOException;

import android.app.Activity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;

public class MainActivity extends Activity {
	//Remount /system as rw
	private static final String REMOUNT_RW = "mount -o rw,remount -t ext4 /dev/block/platform/omap/omap_hsmmc.0/by-name/system /system" + "\n";
	
	//Remount /system as ro
	private static final String REMOUNT_RO = "mount -o ro,remount -t ext4 /dev/block/platform/omap/omap_hsmmc.0/by-name/system /system" + "\n";
	
	//modify model name in /system/build.prop by redirect content
	private static final String MODIFY_MODEL_NAME = "cat /sdcard/build.prop > /system/build.prop" + "\n";
	
	//reboot to enable the modification
	private static final String REBOOT = "reboot" + "\n";

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		//get root access and remount /system as 'rw'
		try {
			Process process = Runtime.getRuntime().exec("su");
			DataOutputStream os = new DataOutputStream(process.getOutputStream());
			os.writeBytes(REMOUNT_RW);
			os.writeBytes(MODIFY_MODEL_NAME);
			os.writeBytes(REMOUNT_RO);
			os.writeBytes("exit\n");
			os.flush();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		// Handle action bar item clicks here. The action bar will
		// automatically handle clicks on the Home/Up button, so long
		// as you specify a parent activity in AndroidManifest.xml.
		int id = item.getItemId();
		if (id == R.id.action_settings) {
			return true;
		}
		return super.onOptionsItemSelected(item);
	}
}
