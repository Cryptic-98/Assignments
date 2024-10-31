const fill_name = document.getElementById("fullName").value;
const fill_number = document.getElementById("phoneNumber").value;
const fill_email = document.getElementById("emailAddress").value;
const fill_attendees = document.getElementById("numberOfAttendees").value;
const fill_time = document.getElementById("arrivalTime").value;
const fill_menu = document.getElementById("menuPreference").value;
const fill_table = document.getElementById("tableOption").value;

function submit() {
  document.getElementById("fill_name").innerHTML = "Full Name: " + fill_name;
  document.getElementById("fill_number").innerHTML =
    "Phone Number: " + fill_number;
  document.getElementById("fill_email").innerHTML = "Email: " + fill_email;
  document.getElementById("fill_attendees").innerHTML =
    "Number of Attendees: " + fill_attendees;
  document.getElementById("fill_time").innerHTML = "Arrival Time: " + fill_time;
  document.getElementById("fill_menu").innerHTML =
    "Menu Preference: " + fill_menu;
  document.getElementById("fill_table").innerHTML =
    "Table Option: " + fill_table;
}
