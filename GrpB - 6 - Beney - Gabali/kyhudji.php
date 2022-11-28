<!DOCTYPE html>
<html lang="fr">
  <head>
    <title>Portfolio de GigaChad</title>
    <meta name="description" content="Ce site est un Portfolio de William Gabali et de Dylan Beney, deux GigaChad">
    <!--Import Google Icon Font-->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <!--Import materialize.css-->
    <link type="text/css" rel="stylesheet" href="css/materialize.css"  media="screen,projection">
    <link type="text/css" rel="stylesheet" href="css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Modern+Antiqua&display=swap" rel="stylesheet">
    <meta charset="utf-8">
    <!--Let browser know website is optimized for mobile-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  </head>

  <body>
    <header>
      <nav>
        <div class="nav-wrapper black">
          <a href="index.html"  class="brand-logo center" ><img class="logo" src="https://pbs.twimg.com/profile_images/1567358240224153600/iHuX-JWg_400x400.jpg" alt="Logo de William"></a>
          <ul id="nav-mobile" class="right hide-on-med-and-down">
            <li><a href="kyhudji.html">Kyhudji.gg</a></li>
            <li><a href="squadhost_.html">SquadHost_</a></li>
          </ul>
          <ul id="slide-out" class="sidenav">
            <li><div class="user-view">
            <div class="background">
                <img src="img/Kyhudji_background.jpg" alt="Background de la side nav">
            </div>
            <a href="https://gamingcampus.fr"><i><img class="circle" src="https://img-cdn.tnwcdn.com/image?url=https%3A%2F%2Fpbs.twimg.com%2Fprofile_images%2F1267815531391770625%2FcAGe24Ly.jpg&signature=bd635c392b10c6a4ef378e48e4ce42f0" alt="Logo du Gaming Campus"></i></a>
            <span class="white-text name">Gabali William</span>
            <span class="white-text email">williamgabali@gaming.tech</span></div></li>
            <li class="kyhudji"><a href="kyhudji.html"><i><img src="https://pbs.twimg.com/profile_images/1567358240224153600/iHuX-JWg_400x400.jpg" alt="Logo de william"></i>Kyhudji.gg</a></li>
            <li class="squadhost_nav"><a href="squadHost_.html"><i><img src="img/logo.PNG" alt="Logo de Dylan"></i>SquadHost_</a></li>
          </ul>
        <a href="#" data-target="slide-out" class="sidenav-trigger"><i class="material-icons">menu</i></a>
       </div>
      </nav>
    </header>
    <div class="body">
      <div class="title">
        <div class="h1">
            <h1>Gabali William</h1>
        </div>
      </div>
    </div>
    <div class="row row-william">
      <h2 class="col s12">Présentation</h2>
          <div class="col l6 m6 s12" id="trigger-wg"><img class="william" src="img/william.jpg" alt="photo de william"></div>
          <div class="col l6 m6 s12">je m'appèle Gabali William j'ai 20 ans et je suis étudiant au Gaming Campus a lyon
            pour suivre une formation pour pouvoir travailler dans le domaine du jeux vidéo en tant que Game developpeur 
            ou Game designer.
      </div>
    </div>
    <div class="skills-william">
        <div class="skill-bar white-text">
          <h3>Mes Compétences</h3>
          <p>HTML</p>
          <div class="skills-container white-text">
            <div class="skills html">55%</div>
          </div>
          
          <p>CSS</p>
          <div class="skills-container white-text">
            <div class="skills css">60%</div>
          </div>
          
          <p>JavaScript</p>
          <div class="skills-container white-text">
            <div class="skills js">25%</div>
          </div>
          
          <p>PHP</p>
          <div class="skills-container white-text">
            <div class="skills php">15%</div>
          </div>

          <p>SQL</p>
          <div class="skills-container white-text">
            <div class="skills sql">10%</div>
          </div>
      </div>
    </div>
      <div class="carousel carousel-slider center dylan">
        <div class="carousel-item Kyhu1 white-text" >
          <h2>Esport Rocket League</h2>
          <p class="white-text">Mon expérience en esports Rocket league</p>
          <div class="carousel-fixed-item center">
            <a class="btn waves-effect white grey-text darken-text-2" href="https://www.start.gg/user/baed09d1">button</a>
          </div>
        </div>
        <div class="carousel-item Kyhu2 white-text" >
          <h2>Esport Valorant</h2>
          <p class="white-text">Mon espérience en esports VALORANT</p>
          <div class="carousel-fixed-item center">
            <a class="btn waves-effect white grey-text darken-text-2" href="https://tracker.gg/valorant/profile/riot/TLN%20Kyhudji%23KYJ/overview">button</a>
          </div>
        </div>
        <div class="carousel-item Kyhu3 white-text">
          <h2>Esport TrackMania</h2>
          <p class="white-text">Mon espérience en esports TrackMania</p>
          <div class="carousel-fixed-item center">
            <a class="btn waves-effect white grey-text darken-text-2" href="https://trackmania.io/#/player/2c978b8b-833e-45ac-b856-c0d674a7f55b">button</a>
          </div>
        </div>
      </div>
      <footer class="page-footer">
            <div class="container">
              <div class="row">
                <div class="col l6 s12">
                  <h5 class="white-text">Conclusion</h5>
                  <p class="grey-text text-lighten-4">clique pour devenir un <a href="gigachad.html">Gigachad</a></p>
                </div>
                <div class="col l4 offset-l2 s12 footer">
                    <!-- Modal Trigger -->
                    <a class="waves-effect waves-light btn modal-trigger black" href="#modal1">Contactez nous</a>
        
                    <!-- Modal Structure -->
                    <div id="modal1" class="modal">
                      <div class="modal-content">
                        <div class="container">
                        
                            <label for="fname">Prénom</label>
                            <input type="text" id="fname" name="firstname" placeholder="Votre prénom de GigaChad...">
                        
                            <label for="lname">Nom</label>
                            <input type="text" id="lname" name="lastname" placeholder="Votre nom de GigaChad...">
                        
                            <label for="subject">E.Mail</label>
                            <textarea id="subject" name="subject" placeholder="Un E.Mail de Chad"></textarea>
                        
                            <input class="submit" type="submit" value="Envoyer">
                        
                        </div>
                      </div>
                      <div class="modal-footer">
                        <a href="#!" class="modal-close waves-effect waves-green btn-flat">Accepter</a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            <div class="footer-copyright">
            <div class="container">
            © Copyright Les deux GigaChad appeler Dylan Beney et William Gabali
        </div>
        </div>
      </footer>
    <script type="text/javascript" src="js/JqueryMin.js"></script>
    <!--JavaScript at end of body for optimized loading-->
    <script type="text/javascript" src="js/materialize.min.js"></script>
    <script type="text/javascript" src="js/script.js"></script>
  </body>
</html>