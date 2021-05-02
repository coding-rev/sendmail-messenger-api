// ===============================
//Fetching from an API (GET)
// ==============================
// function ssmGET(){
// 	fetch('http://127.0.0.1:8000/')
// 		.then(results => results.json())
// 		.then(console.table)
// }

// ================================
// Sending to an API (POST)
// =================================
function ssmPOST(){
	// Setting recipient and sender email
	const recipient_email = "emmowu10@gmail.com";
	const sender_email    = "emmowu10@gmail.com";

	// Getting user's Inputs
	var form_name 		= document.getElementById('form_name').value; 
	var form_subject 	= document.getElementById('form_subject').value;
	var form_message 	= document.getElementById('form_message').value;
	var form_email 		= document.getElementById('form_email').value;
	var attachment 		= document.getElementById('attachment');

	// Presenting to suit API request (JSON)
	const data = 
	 {
        "form_name": form_name,
        "form_subject": form_subject,
        "form_message": form_message,
        "form_email": form_email,
        "sender_email": sender_email,
        "recipient_email": recipient_email,
        "attachment": attachment,
    };
    
	fetch('http://127.0.0.1:8000/', { method: 'POST', body: data})
		.then(results => results.json())
		.then(console.log)
}