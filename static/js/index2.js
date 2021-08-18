
document.querySelector('#form-example').addEventListener('submit', function(event){
	event.preventDefault()

	// Cara 1
	// var email = document.querySelector("input[name='email']").value
	// var password = document.querySelector("#exampleInputPassword1").value
	// console.log(email)
	// console.log(password)

	// fetch('/submit-form', {
	// 	headers: {
	// 		'Content-Type': 'application/json'
	// 	},
	// 	method: 'POST',
	// 	// body  : {'email': email, 'password': password}, 
	// 	// body  : {email: email, password: password}
	// 	body: JSON.stringify({email, password}),
	// })

	// Cara 2
	// this === document.querySelector('#form-example')
	var formData = new FormData(this) // hanya utk <form>

	fetch('/submit-form', {

		method: 'POST',
		body: formData,
	})

	// Cara 3
	var email = document.querySelector("input[name='email']").value
	var password = document.querySelector("#exampleInputPassword1").value

	// Checking email and password
	// bla bla

	var formData2 = new FormData()

	// formData2.append('key', 'value')
	formData2.append('email', email)
	formData2.append('password', password)
	fetch('/submit-form', {
		method: 'POST',
		body: formData2,
	})

})

