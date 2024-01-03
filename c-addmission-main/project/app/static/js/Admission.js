const Validate = () => {
  var Stud_name = document.querySelector(".Stud_Name");
  var Surname = document.querySelector(".Stud_surname");
  var Father = document.querySelector(".Father_name");
  var Mother = document.querySelector(".Mother_name");
  var n = document.querySelector("#s1");
  var n1 = document.querySelector("#s2");

  if (Stud_name.value === "" || Stud_name.value.length <= 3 || Surname.value === "" || Surname.value.length <= 3) {
    n.style.display = "inline";
    n.innerHTML = "Should be more than 3 letters"; 
  } else {
    n.style.display = "none";
  }

  if (Father.value === "" || Father.value.length <= 3 || Mother.value === "" || Mother.value.length <= 3) {
    n1.style.display = "inline";
    n1.innerHTML = "Should be more than 3 letters"; 
  } else {
    n1.style.display = "none";
  }
}
