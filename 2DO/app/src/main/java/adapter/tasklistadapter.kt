package adapter

import android.app.Activity
import android.content.Context
import android.database.sqlite.SQLiteDatabase.openOrCreateDatabase
import android.view.View
import android.view.ViewGroup
import android.widget.ArrayAdapter
import android.widget.CheckBox
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.a2do.R
import model.TaskModel

class tasklistadapter(
    private val activity: Activity,
    private val objects: Array<TaskModel>
) : ArrayAdapter<TaskModel>(activity, R.layout.tasklist, objects) {

    override fun getView(position: Int, convertView: View?, parent: ViewGroup): View {
        var view: View? = convertView
        val viewHolder: ViewHolder

        if (view == null) {
            view = activity.layoutInflater.inflate(R.layout.tasklist, parent, false)

            viewHolder = ViewHolder()
            viewHolder.name = view.findViewById(R.id.task)
            viewHolder.checkBox = view.findViewById(R.id.checkbox)
            view.tag = viewHolder
        } else {
            viewHolder = view.tag as ViewHolder
        }


        viewHolder.name.text = objects[position].task
        viewHolder.checkBox.contentDescription = objects[position].id.toString()

        view?.contentDescription = objects[position].id.toString()
        viewHolder.checkBox.setOnCheckedChangeListener { buttonView, isChecked ->
            deleteTask.add(viewHolder.checkBox.contentDescription.toString())
        }
        return view!!
    }

    companion object {
        class ViewHolder {
            lateinit var name: TextView
            lateinit var checkBox: CheckBox
        }
        var deleteTask:ArrayList<String> = arrayListOf()
    }
}
