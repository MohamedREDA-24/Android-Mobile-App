package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class SignUp_activity extends AppCompatActivity {

    Button btnSign_up;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.sign_up_activity);
        btnSign_up=findViewById(R.id.btnSignUp);
        btnSign_up.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(SignUp_activity.this, "Signed Up Successfully", Toast.LENGTH_SHORT).show();
                Intent goToLogin = new Intent(SignUp_activity.this,MainActivity.class);
                startActivity(goToLogin);
            }

        });
    }
}