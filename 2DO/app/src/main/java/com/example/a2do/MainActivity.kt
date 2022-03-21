package com.example.a2do

import adapter.tasklistadapter
import android.content.Intent
import android.database.sqlite.SQLiteException
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.view.View
import android.widget.*
import com.google.android.material.floatingactionbutton.FloatingActionButton
import model.TaskModel

class MainActivity : AppCompatActivity() {
    private lateinit var notask:TextView
    private lateinit var notaskdetails:TextView
    private lateinit var btnlogin:Button
    private lateinit var btnadd:FloatingActionButton
    private lateinit var btndelete:Button
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        notask = findViewById(R.id.notask)
        notaskdetails = findViewById(R.id.notasksdetails)
        btnlogin = findViewById(R.id.btnlogin)
        btnadd = findViewById(R.id.fbtnaddtask)
        btndelete = findViewById(R.id.btndelete)
        val tasklist = findViewById<ListView>(R.id.tasklist)
        val userid = getSharedPreferences("ToDo", MODE_PRIVATE).getInt("UserId",0)
            val taskarray = gettasks()
        if(userid == 0){
            notask.text = "Login To See Your Tasks"
            notaskdetails.visibility = View.GONE
            btnlogin.visibility = View.VISIBLE
            btnadd.visibility = View.GONE
            btndelete.visibility = View.GONE
            btnlogin.setOnClickListener {
                startActivity(Intent(this,Login_Activity::class.java))
            }
        }
        else if(taskarray.isEmpty())
        {
            notask.text = "NO TASKS"
            notaskdetails.text = "You can create new tasks \n  by using + button"
        }
        val adapter = tasklistadapter(this,taskarray)
        tasklist.adapter = adapter
        tasklistadapter.deleteTask
        btndelete.setOnClickListener {
            deletetask()
            this.recreate()
        }
        btnadd.setOnClickListener {
            val intent = Intent(this,AddTaskActivity::class.java)
            startActivity(intent)
        }
    }

    private fun gettasks(): Array<TaskModel>
    {
        val userid = getSharedPreferences("ToDo", MODE_PRIVATE).getInt("UserId",0)
        val taskarray = arrayListOf<TaskModel>()
        try
        {
            val db = openOrCreateDatabase("ToDo", MODE_PRIVATE, null)
            val query =
                "SELECT * FROM taskdetails WHERE UserId = $userid"
            val cursor = db.rawQuery(query,null)
            while (cursor.moveToNext())
            {
                val taskdata = TaskModel(
                    cursor.getInt(0),
                    cursor.getString(1)
                )
                taskarray.add(taskdata)
            }
            cursor.close()
            db.close()
        }
        catch (ex: SQLiteException)
        {
            Toast.makeText(this, ex.message!!, Toast.LENGTH_SHORT).show()

        }
        return  taskarray.toTypedArray()
    }
    private fun deletetask()
    {
        try
        {
            val db = openOrCreateDatabase("ToDo", MODE_PRIVATE, null)
            val tasks = tasklistadapter.deleteTask
            for(task in tasks)
            {
                db.delete("taskdetails","Id=?", arrayOf(task))
                db.delete("reminder","TaskId=?", arrayOf(task))
            }
            db.close()
        }
        catch (ex: SQLiteException)
        {
            Toast.makeText(this, ex.message!!, Toast.LENGTH_SHORT).show()

        }
    }
    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        val userid = getSharedPreferences("ToDo", MODE_PRIVATE).getInt("UserId",0)
        menuInflater.inflate(R.menu.menu_main, menu)
        val login = menu?.findItem(R.id.login)
        val logout = menu?.findItem(R.id.logout)
        if(userid!=0)
        {
            login?.isVisible = false
        }
        else
        {
            logout?.isVisible = false
        }
        return super.onCreateOptionsMenu(menu)
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
            when (item.itemId) {
                R.id.logout -> {
                    val sp = getSharedPreferences("ToDo", MODE_PRIVATE)
                    val editor = sp.edit()
                    editor.remove("UserId")
                    editor.clear()
                    editor.apply()
                    this.recreate()
                    return true
                }
            }
            when (item.itemId) {
                R.id.login -> {
                    val intent = Intent(this, Login_Activity::class.java)
                    startActivity(intent)
                    finish()
                    return true
                }
            }
        return false
    }
}