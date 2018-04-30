function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

function displayPage() {
	document.getElementById("question").innerHTML = '<h3>' + fc.flashcards_id + '. ' + fc.question + '</h3>';
		
	for (let i = 0; i < numAnswers; i++) {
		document.getElementById(ANSWER_KEYS[i]).innerHTML = '<p>' + fc.answers[answerKeys[i]] + '</p>';
	}
}

function getResult(clickedElement) {
	if (!clicked) {
		var clickedAnswer = clickedElement.innerHTML.slice(3,-4);
		if (clickedAnswer == correctValue) {
			clickedElement.style.backgroundColor = 'green'; 
		}
		else {
			clickedElement.style.backgroundColor = 'red';
		}
		// set tooltip on question
		document.getElementById('question').title = fc.definition;
		clicked = true;
	}
}

// var correctValue = fc.answers.answer_a;
// shuffleArray(answerKeys);
// clicked = false;
// displayPage();
// var flashcards = [{"id":1,"question":"adept","answer_a":"skillful","answer_b":"speedy","answer_c":"attractive","answer_d":"unsophisticated"},{"id":2,"question":"huge","answer_a":"big","answer_b":"slow","answer_c":"ugly","answer_d":"spicy"}];

var f = FLASHCARDS;
// var fc = JSON.parse(f);
document.getElementById("question").innerHTML = f;

// var f = "'" + FLASHCARDS + "'";
// var fc = JSON.parse(f);
// document.getElementById("question").innerHTML = fc;

// var fc = JSON.parse(JSON.stringify(FLASHCARDS));



