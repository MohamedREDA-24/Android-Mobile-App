package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    TextView txforgetPass;
    TextView txcreateAcc;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        txforgetPass = findViewById(R.id.txt_forgetPass);
        txforgetPass.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent goToForgetPass =new Intent(MainActivity.this,ForgetPasswordActivity.class);
                startActivity(goToForgetPass);
            }
        });
        txcreateAcc=findViewById(R.id.txt_creatAcc);
        txcreateAcc.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent goToCreateAcc = new Intent(MainActivity.this,SignUp_activity.class);
                startActivity(goToCreateAcc);
            }
        });
    }
}