package com.example.a2do

import android.app.*
import android.content.Context
import android.content.Intent
import android.database.sqlite.SQLiteException
import android.os.Build
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.*
import androidx.annotation.RequiresApi
import java.text.DateFormat
import java.util.*

class AddTaskActivity : AppCompatActivity(), DatePickerDialog.OnDateSetListener,
    TimePickerDialog.OnTimeSetListener {
    private lateinit var etaddtask: EditText
    private var day = 0
    private var month = 0
    private var year = 0
    private var hour = 0
    private var minute = 0
    private var savedday = 0
    private var savedmonth = 0
    private var savedyear = 0
    private var savedhour = 0
    private var savedminute = 0

    @RequiresApi(Build.VERSION_CODES.O)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_add_task)
        createtabletask()
        pickDate()
        val btnaddtask = findViewById<Button>(R.id.btnaddtask)
        etaddtask = findViewById(R.id.etdaddtask)
        createNotificationChannel()
        btnaddtask.setOnClickListener {

            addtask()
            sheduleNotification()
            val intent = Intent(this, MainActivity::class.java)
            startActivity(intent)
        }

    }

    private fun sheduleNotification() {
        val intent = Intent(applicationContext, Notification::class.java)
        val title = "Reminder"
        val message = "Complete The Task"
        intent.putExtra(titleExtra, title)
        intent.putExtra(messageExtra, message)

        val pendingIntent = PendingIntent.getBroadcast(
            applicationContext,
            notificationId,
            intent,
            PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT
        )
        val alarmManager = getSystemService(Context.ALARM_SERVICE) as AlarmManager
        val calendar = Calendar.getInstance()
        calendar.set(savedyear, savedmonth, savedday, savedhour, savedminute)
        val time = calendar.timeInMillis
        alarmManager.setExactAndAllowWhileIdle(
            AlarmManager.RTC_WAKEUP,
            time,
            pendingIntent
        )
        showAlert(time, title, message)
    }

    private fun showAlert(time: Long, title: String, message: String) {
        val dt = Date(time)
        val dtformat = android.text.format.DateFormat.getLongDateFormat(applicationContext)
        val timeformat = android.text.format.DateFormat.getTimeFormat(applicationContext)

        AlertDialog.Builder(this)
            .setTitle("TODO")
            .setMessage(
                "Title: " + title +
                        "Message: " + message +
                        "At: = " + dtformat.format(dt) + " " + timeformat.format(dt)
            )
            .setPositiveButton("Okay") { _, _ -> }
            .show()


    }

    @RequiresApi(Build.VERSION_CODES.O)
    private fun createNotificationChannel() {
        val name = "notif name"
        val desc = "random"
        val importance = NotificationManager.IMPORTANCE_DEFAULT
        val channel = NotificationChannel(channelId, name, importance)
        channel.description = desc
        val notificationManager = getSystemService(NOTIFICATION_SERVICE) as NotificationManager
        notificationManager.createNotificationChannel(channel)
    }

    private fun createtabletask() {
        val db = openOrCreateDatabase("ToDo", MODE_PRIVATE, null)
        try {
            val createTableTaskDetails =
                "Create table IF NOT EXISTS taskdetails(Id INTEGER PRIMARY KEY AUTOINCREMENT, TaskDescription TEXT , UserId INTEGER,time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,CONSTRAINT fk_userid FOREIGN KEY (UserId)REFERENCES userdetails(Id))"
            db.execSQL(createTableTaskDetails)
            val createTableRemainder =
                "Create table IF NOT EXISTS reminder( reminderid INTEGER PRIMARY KEY AUTOINCREMENT, Date TEXT , Hour Text,Minute Text, TaskId INTEGER,CONSTRAINT fk_taskid FOREIGN KEY (TaskId)REFERENCES taskdetails(Id))"
            db.execSQL(createTableRemainder)
            db.close()

        } catch (ex: SQLiteException) {
            println(ex)
        }

    }

    private fun addtask()
    {
        val userid = getSharedPreferences("ToDo", MODE_PRIVATE).getInt("UserId",0)
        try {
            val taskdesc = etaddtask.text.toString()


            val db = openOrCreateDatabase("ToDo", MODE_PRIVATE, null)
            val query =
                "Insert into taskdetails(TaskDescription,UserId)VALUES('$taskdesc',$userid)"
            db.execSQL(query)
            val selectLastId = "SELECT  * FROM taskdetails"
            val cursor = db.rawQuery(selectLastId, null)
            cursor.moveToLast()
            val id: Int = cursor.getInt(0)
            val insertReminder =
                "INSERT INTO reminder(Date,Hour,Minute,Taskid)VALUES('$day-${month+1}-$year',$hour,$minute,$id)"
            db.execSQL(insertReminder)
            Toast.makeText(this, "Tasks Added", Toast.LENGTH_SHORT).show()
            cursor.close()
            db.close()
        } catch (ex: SQLiteException) {
            Toast.makeText(this, ex.message!!, Toast.LENGTH_SHORT).show()

        }
    }

    private fun getDateTimeCalendar() {
        val calendar = Calendar.getInstance()
        day = calendar.get(Calendar.DAY_OF_MONTH)
        month = calendar.get(Calendar.MONTH)
        year = calendar.get(Calendar.YEAR)
        hour = calendar.get(Calendar.HOUR)
        minute = calendar.get(Calendar.MINUTE)
    }

    private fun pickDate() {
        findViewById<Button>(R.id.btnsettimeanddate).setOnClickListener {
            getDateTimeCalendar()
            DatePickerDialog(this, this, year, month, day).show()
            findViewById<TextView>(R.id.showTimeAndDate).text =
                "Selected Time Is ${hour}:${minute} \n Selected Date Is ${day}-${month}-${year}"
        }
    }

    override fun onDateSet(p0: DatePicker?, year: Int, month: Int, dayOfmonth: Int) {
        savedday = dayOfmonth
        savedmonth = month
        savedyear = year
        getDateTimeCalendar()

        TimePickerDialog(this, this, hour, minute, false).show()
    }

    override fun onTimeSet(p0: TimePicker?, hourofday: Int, minute: Int) {
        savedhour = hourofday
        savedminute = minute
    }

}