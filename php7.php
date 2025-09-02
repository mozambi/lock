<?php
date_default_timezone_set("Asia/Kolkata");

if(isset($_COOKIE["lastVisit"])){
    $lastVisit=$_COOKIE["lastVisit"];
}else{
    $lastVisit="this is your first visit";
}
$currentTime=date("Y-m-d H:i:s");
setcookie("lastVisit",$currentTime,time()+(365*24*60*60));
?>


<!DOCTYPE html>
<html>
<head>
<title>PSGCAS-HOME</title>
<style>
body{
    margin:0;
    font-family:Arial,sans-serif;
    color:white;
    background:url("https://media.getmyuni.com/azure/college-image/big/psg-college-of-arts-and-science-psgcas-coimbatore.jpg") no-repeat center center/cover;
}
.overlay{
    background:rgba(0,0,0,0.6);
    min-height:100vh;
    padding:20px;
}
header,footer{
    text-align:center;
}
header h1{font-size:32px;margin:0;}
header p{font-size:18px;margin:5px 0 20px;}

nav{text-align:right;margin:20px 0;}
nav a{
    color:yellow;
    margin:0 15px;
    text-decoration:none;
    font-weight:bold;
}
nav a:hover{text-decoration:underline;}
section{
    max-width:800px;
    margin:20px auto;
    padding:15px;
    background:rgba(255,255,255,0.1);
    border-radius:8px;
}
section h2{color:yellow;}
footer{
    padding:10px;
    background:rgba(0,0,0,0.7);
    position:fixed;
    bottom:0;
    width:100%;
}
</style>
</head>
<body>
<div class="overlay">
<header>
<h1>WELCOME TO PSGCAS</h1>
<p>EXCELLENCE IN EDUCATION</p>
</header>
<nav>
<a href="https://www.psgcas.ac.in/">Home</a>
<a href="https://applications.psgcas.ac.in/">Admission</a>
<a href="https://www.psgcas.ac.in/departments/">Department</a>
<a href="https://psgcas-dl.knimbus.com/portal/v2/default/home">Library</a>
<a href="https://www.psgcas.ac.in/">Contact</a>
</nav>
<section>
<h2>About PSGCAS</h2>
<p>
PSGCAS,coimbatore is one of the prestigious institution in tamilnadu.which offers a wide variety of 
UG,PG & research programs
</p>
</section>
<section>
<h2>vision & mission</h2>
<p>
Our vision is to provide world class education and 
froster research,innovationand holistic development to serve society
</p>
</section>
<footer>
<p>&copy;<?php echo date("Y"); ?> PSGCAS|ALL RIGHTS RESERVED</p>
<p style="color:white;">your last visit on this page is<?php echo $lastVisit;?></p> 
</footer>
</div>

</body>
</html>

