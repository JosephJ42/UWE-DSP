package com.example.identiflora

import android.content.Context
import android.database.Cursor
import android.database.SQLException
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper
import android.util.Log
import java.io.FileOutputStream
import java.io.IOException

class PlantDatabaseHandler (context:Context): SQLiteOpenHelper(context, "plantInformation.db", null, 1){

    var dbName = "plantInformation.db"
    var dbLocation = context.getDatabasePath(dbName).absolutePath
    private var DataBase: SQLiteDatabase? = null
    var context = context


    override fun onCreate(db: SQLiteDatabase?) {
    }

    override fun onUpgrade(db: SQLiteDatabase?, oldVersion: Int, newVersion: Int) {
    }

    override fun onOpen(db: SQLiteDatabase?) {
        super.onOpen(db)
    }


    // Open the database, so we can read from it.
    @Throws(SQLException::class)
    fun openDataBase(): SQLiteDatabase? {

        this.readableDatabase
        try {
            copyDataBase()
        } catch (e: IOException) {
            throw Error("Error copying database")
        }


        DataBase = SQLiteDatabase.openDatabase(dbLocation, null, SQLiteDatabase.OPEN_READWRITE)
        return DataBase
    }

    //Creates a copy in memory of the database from the assets file
    @Throws(IOException::class)
    private fun copyDataBase() {

        val inputStream = context.assets.open(dbName)
        val databaseOutputStream = FileOutputStream(dbLocation)
        val buffer = ByteArray(1024)

        while ( inputStream.read(buffer) > 0) {
            databaseOutputStream.write(buffer)
        }

        databaseOutputStream.flush()
        databaseOutputStream.close()
        inputStream.close()

    }

//    fun getPlantInforFromName(db: SQLiteDatabase?): Cursor? {
//
//        val db = this.readableDatabase
//        return db.rawQuery("SELECT * From plantInfo", null)
//
//    }


    companion object{
        // here we have defined variables for our database
        private val DATABASE_NAME = "plantInformation"
        private val DATABASE_VERSION = 1
        val table = "plantInfo"


        //plant_name TEXT PRIMARY KEY, plant_description TEXT, watering TEXT, light_levels TEXT, ideal_temperature TEXT, ideal_humidity TEXT, feeding_and_fertilizing TEXT, special_information TEXT

       public val idCol = "plant_name"
        val descriptionCol = "plant_description"
        val waterCol = "watering"
        val lightCol = "light_levels"
        val tempCol = "ideal_temperature"
        val humidityCol = "ideal_humidity"
        val feedingCol = "feeding_and_fertilizing"
        val specialInfoCol = "special_information"
    }




}



