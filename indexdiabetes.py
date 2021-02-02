# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 20:42:13 2020

@author: Sai Viswa
"""


<!DOCTYPE html>

<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Diabetes Predictor</title>
        <link rel="shortcut icon" href="{{ url_for('static', filename='diabetes-favicon.ico') }}">
        <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles.css') }}">
        <script src="https://kit.fontawesome.com/5f3f547070.js" crossorigin="anonymous"></script>
        <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
    </head>

    <body>

        <!-- Website Title -->
    	<div class="container">
            <h2 class='container-heading'><span class="heading_font">Diabetes Predictor</span></h2>
            <div class='description'>
    			<p>A Machine Learning Web App, Built with Flask, Deployed using Heroku.</p>
    		</div>
    	</div>

        <!-- Text Area -->
    	<div class="ml-container">
    		<form action="{{ url_for('predict') }}" method="POST">
                <input class="form-input" type="text" name="pregnancies" placeholder="Number of Pregnancies eg. 0"><br>
                <input class="form-input" type="text" name="glucose" placeholder="Glucose (mg/dL) eg. 80"><br>
                <input class="form-input" type="text" name="bloodpressure" placeholder="Blood Pressure (mmHg) eg. 80"><br>
                <input class="form-input" type="text" name="skinthickness" placeholder="Skin Thickness (mm) eg. 20"><br>
                <input class="form-input" type="text" name="insulin" placeholder="Insulin Level (IU/mL) eg. 80"><br>
                <input class="form-input" type="text" name="bmi" placeholder="Body Mass Index (kg/m²) eg. 23.1"><br>
                <input class="form-input" type="text" name="dpf" placeholder="Diabetes Pedigree Function eg. 0.52"><br>
                <input class="form-input" type="text" name="age" placeholder="Age (years) eg. 34"><br>

        		<input type="submit" class="my-cta-button" value="Predict">
        	</form>
    	</div>

        <!-- Footer -->
       <div class='footer'>
           <div class="contact">
               <a target="_blank" href="https://github.com/anujvyas/Diabetes-Prediction-Deployment"><i class="fab fa-github fa-lg contact-icon"></i></a>
               <a target="_blank" href="https://www.linkedin.com/in/anujkvyas"><i class="fab fa-linkedin fa-lg contact-icon"></i></a>
           </div>
           <p class='footer-description'>Made with ❤️ by Anuj Vyas.</p>
       </div>

    </body>
</html>