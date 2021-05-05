// ===============================
//Fetching from an API (GET)
// ==============================
// function ssmGET(){
// fetch('https://simplysendmail.herokuapp.com')
// 	.then(results => results.json())
// 	.then(console.table)
// }
// ssmGET();

// ================================
// Sending to an API (POST)
// =================================
function ssmPOST(){
	// Setting recipient and sender email
	const recipient_email_val = "emmowu10@gmail.com";
	const sender_email_val    = "emmowu10@gmail.com";

	// Getting user's Inputs
	var form_name_val 		= document.getElementById('form_name').value; 
	var form_subject_val 	= document.getElementById('form_subject').value;
	var form_message_val 	= document.getElementById('form_message').value;
	var form_email_val 		= document.getElementById('form_email').value;
	// var attachment_file		= document.getElementById('attachment');

	// data to be sent to the POST request
	let _data = {
        "form_name" : form_name_val,
        "form_subject": form_subject_val,
        "form_message": form_message_val,
        "form_email": form_email_val,
        "sender_email": sender_email_val,
        "recipient_email": recipient_email_val,
        // "attachment": attachment_file
    }
    
	fetch('https://simplysendmail.herokuapp.com', {
	  method: "POST",
	  body: JSON.stringify(_data),
	  headers: {"Content-type": "application/json; charset=UTF-8"}
	})
	.then(response => response.json()) 
	.then(json => console.log(json))
	// .catch((error) => {
 //  		console.error('Error:', error);
	// });
	
}

