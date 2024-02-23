function clicked() {
    var input = document.getElementById("in").value;
    findInPage(input)
}


function findInPage(str) {
    var txt, i, found;
    if (str=="") return false;
   
    if ((document.layers)||(window.sidebar)) {
      if (!window.find(str)) {
        alert("Fin de page atteinte.\n"+'"'+str+'" trouvé '+nbSearch+" fois.");
        while(window.find(str, false, true)) {nbSearch++;}
      } 
      else
        nbSearch++;
      if (nbSearch == 0)
        alert('"'+str+'" est introuvable');
    }
   
    if (document.all) {
      txt = window.document.body.createTextRange();
      for (i = 0; i <= nbSearch && (found = txt.findText(str)) != false; i++) {
        txt.moveStart("character", 1);
        txt.moveEnd("textedit");
      }
      if (found) {
        txt.moveStart("character", -1);
        txt.findText(str);
        txt.select();
        txt.scrollIntoView();
        nbSearch++;
      } else {
        if (nbSearch > 0) {
              alert("Fin de page atteinte.\n"+'"'+str+'" trouvé '+nbSearch+" fois.");
   
          nbSearch = 0;
          findInPage(str);
        } else { 
          alert('"'+str+'" est introuvable');
        }
      }
    }
   
    return false;
  }