package com.example.a2do

import android.annotation.SuppressLint
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast

class Login_Activity : AppCompatActivity() {
    //var regis:Button?=null
    private var login: Button? = null
    private var mail: EditText?=null
    private var pwrd:EditText?=null
    private var linkbutton: TextView?=null


    @SuppressLint("Recycle")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

//        regis= findViewById<Button>(R.id.btnregnow)
        login= findViewById(R.id.btnlogin)
        mail=findViewById(R.id.etem)
        pwrd=findViewById(R.id.etpwrd)
        linkbutton=findViewById(R.id.tvinfo)
        linkbutton!!.setOnClickListener{
            val intent= Intent(this,Register_Actitvity::class.java)
            startActivity(intent)
            // Toast.makeText(this, "LOADING...", Toast.LENGTH_SHORT).show()
        }

        val sp = getSharedPreferences("ToDo", MODE_PRIVATE)

        if(sp.contains("Id"))
        {
//            var abc = sp.
            val intent= Intent(this, MainActivity::class.java)
            startActivity(intent)
            finish()
        }
        else
        {
            login!!.setOnClickListener{
//                Toast.makeText(this, "Logging in.. ", Toast.LENGTH_SHORT).show()

                val email = mail!!.text.toString()
                val password = pwrd!!.text.toString()


                val db = openOrCreateDatabase("ToDo", MODE_PRIVATE, null)
                val res=db.rawQuery("Select * from userdetails where Email=? and Password=?",  arrayOf(email, password))

                if(res.count > 0)
                {
                    res.moveToFirst()
//                    val abc = res.getInt(0)
//                    Log.i("error",abc.toString())
                    val editor= sp.edit()
                    editor.putInt("UserId", res.getInt(0))
                    editor.apply()

                    //  Toast.makeText(this, "Logged In.. ", Toast.LENGTH_SHORT).show()
                    val intent= Intent(this, MainActivity::class.java)
                    startActivity(intent)
                    finish()
                }
                else
                {
                    Toast.makeText(this, "Wrong Email or Password", Toast.LENGTH_SHORT).show()
                }


            }
        }

    }

}