package com.example.identiflora


import android.content.ActivityNotFoundException
import android.content.Intent
import android.graphics.BitmapFactory
import android.graphics.Color
import android.graphics.drawable.ColorDrawable
import android.media.ExifInterface
import android.os.Bundle
import android.os.Environment
import android.provider.MediaStore
import android.view.View
import android.widget.ImageButton
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.FileProvider
import com.example.identiflora.ml.IdentiFloraCNNModel
import org.tensorflow.lite.DataType
import org.tensorflow.lite.support.image.ImageProcessor
import org.tensorflow.lite.support.image.TensorImage
import org.tensorflow.lite.support.image.ops.ResizeOp
import org.tensorflow.lite.support.tensorbuffer.TensorBuffer
import java.io.File


//Constants
private const val REQUEST_IMAGE_CAPTURE = 123
private lateinit var plantPhotoFile: File
private const val fileName ="plant.jpg"


class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        //Changes colour of Action bar (This seems to be the only way of doing this)
        supportActionBar!!.setBackgroundDrawable(ColorDrawable(Color.parseColor("#4C9A2A")))

    }

    //Opens Camera on button
    fun openCamera(view: View) {

        plantPhotoFile = getPhotoFile(fileName)
        val takePictureIntent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
        val fileProvider =
            FileProvider.getUriForFile(this, "com.example.identiflora.fileprovider", plantPhotoFile)
        takePictureIntent.putExtra(MediaStore.EXTRA_OUTPUT, fileProvider)

        if(takePictureIntent.resolveActivity(this.packageManager) != null){
            try {
                startActivityForResult(takePictureIntent, REQUEST_IMAGE_CAPTURE)
            } catch (e: ActivityNotFoundException) {
                // display error state to the user
            }
        }
    }

    //gets picture from users file
    private fun getPhotoFile(fileName: String): File {
        val storageLocation = getExternalFilesDir(Environment.DIRECTORY_PICTURES)
        return File.createTempFile(fileName,".jpg", storageLocation)
    }


    // Takes the captures image and passes it through the CNN, returning the name of the plant
    // that the CNN believes the image contains.
    private fun getCNNResults(tensorImage:TensorImage){

        val model = IdentiFloraCNNModel.newInstance(this)

        // Creates inputs for reference.
        val inputFeature0 = TensorBuffer.createFixedSize(intArrayOf(1, 180, 180, 3), DataType.FLOAT32)
        inputFeature0.loadBuffer(byteBuffer)

        // Runs model inference and gets result.
        val outputs = model.process(inputFeature0)
        val outputFeature0 = outputs.outputFeature0AsTensorBuffer

        // Releases model resources if no longer used.
        model.close()


    }

    //
    override fun onActivityResult(requestCode:Int, resultCode:Int, data:Intent?){
        super.onActivityResult(requestCode, resultCode, data)
        if(requestCode == REQUEST_IMAGE_CAPTURE && resultCode == RESULT_OK){

            //Get photos rotation (when it was taken for) for display purposes

            val exifForPlantImage = ExifInterface(plantPhotoFile.absolutePath)
            val orientationOfCamera: Int = exifForPlantImage.getAttributeInt(ExifInterface.TAG_ORIENTATION, ExifInterface.ORIENTATION_NORMAL)

            var angle = 0

            when (orientationOfCamera) {
                ExifInterface.ORIENTATION_ROTATE_90 -> {
                    angle = 90
                }
                ExifInterface.ORIENTATION_ROTATE_180 -> {
                    angle = 180
                }
                ExifInterface.ORIENTATION_ROTATE_270 -> {
                    angle = 270
                }
            }

            val takenImage = BitmapFactory.decodeFile(plantPhotoFile.absolutePath)

            //sets button image as picture, rescaling it and rotating for display purposes
            val imageButtonID = findViewById<ImageButton>(R.id.uploadPlantImageButton)
            imageButtonID.setImageBitmap(takenImage)
            imageButtonID.rotation = angle.toFloat()


            //change instruction text to better reflect what the user is doing in the appication
            val imageCaptionText= findViewById<TextView>(R.id.plantNameText)
            imageCaptionText.setText("Tap the image again to upload a new plant")

            //passed taken image to the CNN

            //val tensorImage = TensorImage.fromBitmap(takenImage)
            //val plantName = getCNNResults(tensorImage)

        }
    }










}





