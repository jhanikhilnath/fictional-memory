const keyPressText = document.querySelector('.key-pressed');

document.addEventListener('keydown', function (e) {
	e.preventDefault();
	console.log(e);
	if (e.key == ' ') {
		keyPressText.textContent = 'space'.charAt(0).toUpperCase() + 'space'.slice(1);
	} else if (e.key == 'Meta') {
		keyPressText.textContent = 'windows'.charAt(0).toUpperCase() + 'windows'.slice(1);
	} else {
		keyPressText.textContent = e.key.charAt(0).toUpperCase() + e.key.slice(1);
	}
});

document.addEventListener('keyup', function () {
	setTimeout(function () {
		keyPressText.textContent = '';
	}, 150);
});
