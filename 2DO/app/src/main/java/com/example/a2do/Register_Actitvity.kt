package com.example.a2do

import android.content.Intent
import android.database.sqlite.SQLiteException
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast

class Register_Actitvity : AppCompatActivity() {
    var name: EditText? = null
    private var contact: EditText? = null
    private var mail: EditText? = null
    private var pwd: EditText? = null
    private var buttonrgs: Button? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_register_actitvity)

        register()
        name = findViewById(R.id.etnm)
        contact = findViewById(R.id.etcon)
        mail = findViewById(R.id.etmail)
        pwd = findViewById(R.id.etpwd)
        buttonrgs = findViewById(R.id.btnrgs)

        buttonrgs!!.setOnClickListener{
            registration()
            val intent= Intent(this,Login_Activity::class.java)
            startActivity(intent)
            finish()
        }


    }
    private fun register() {
        val db = openOrCreateDatabase("ToDo", MODE_PRIVATE, null)
        try {
            val sql =
                "Create table IF NOT EXISTS userdetails(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT , Contact INTEGER , Email TEXT, Password TEXT)"
            db.execSQL(sql)
            db.close()

        } catch (ex: SQLiteException) {
            println(ex)
        }

    }
    private fun registration()
    {
        try
        {
            val nameStr = name!!.text.toString()
            val constr = contact!!.text.toString()
            val mailstr = mail!!.text.toString()
            val pwdstr = pwd!!.text.toString()


            val db = openOrCreateDatabase("ToDo", MODE_PRIVATE, null)
            val query =
                "Insert into userdetails(Name, Contact, Email, Password)VALUES('$nameStr', $constr,'$mailstr','$pwdstr')"
            db.execSQL(query)
            Toast.makeText(this, "Thanks for Registering", Toast.LENGTH_SHORT).show()
            db.close()
        }
        catch (ex: SQLiteException)
        {
            Toast.makeText(this, ex.message!!, Toast.LENGTH_SHORT).show()

        }
    }


}