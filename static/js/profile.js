document.querySelector("#button-get-profile").addEventListener('click', () => {
	fetch('/profile-data',{
		method: 'POST'
	})
	.then((result) => {
		return result.json()
	})
	.then((data)=>{
		// document.querySelector('#name').innerHTML = data.name
		// document.querySelector('#gender').innerHTML = data.gender
		// document.querySelector('#age').innerHTML = data.age
		var list_profile = []

		for (const key in data) {
			if (Object.hasOwnProperty.call(data, key)) {
				list_profile.push(
					`<li class="list-group-item"><div class="row"><div class="col-lg-4"><b>${key}</b></div><div class="col-lg-8">${data[key]}</div></div></li>`
				)
			}
		}

		console.log(list_profile.join('<hr>'))
		document.querySelector("#details").innerHTML = list_profile.join('')

	})
})