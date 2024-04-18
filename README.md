Its probably the most unefficient thing i have ever written. But it works by creating a grid of points that make up a screen and then it marches along the sum of the Camera-Position and the product of the normalized vector between the camera and each gridpoint and a value t which is determined by the min() of the distances of all objects in the scene.
![NormalShading1](https://github.com/QwerMotion/Raymarcher/assets/84264245/c56b069a-9e92-4c73-9330-eeea77b71250)
![NormalShading2](https://github.com/QwerMotion/Raymarcher/assets/84264245/ac71979c-f273-4b8b-be7b-f83136478fad)
