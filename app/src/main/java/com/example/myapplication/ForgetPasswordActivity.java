package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class ForgetPasswordActivity extends AppCompatActivity {

    Button btnsendlink;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_forget_password);
        btnsendlink = findViewById(R.id.btnSendLink);
        btnsendlink.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(ForgetPasswordActivity.this, "Link Sent", Toast.LENGTH_SHORT).show();
            }
        });
    }
}