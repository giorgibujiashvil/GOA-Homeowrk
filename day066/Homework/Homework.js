// //task 1): ### Exercise 1: Create and Append a New Element
// // - **Task**: Create a `<p>` element with the text "Hello World" and append it to the body.
// // - **Methods**: `createElement`, `appendChild`.
// const paragraph = document.createElement('p');

// paragraph.textContent = 'Hello World';
// document.body.appendChild(paragraph);




// //task 2): Exercise 2: Clone and Append an Element
// // - **Task**: Clone an existing `<div>` element and append the clone to the body.
// // - **Methods**: `cloneNode`, `appendChild`.
// // Assume there is an existing <div> with an ID of 'myDiv'
// const originalDiv = document.getElementById('myDiv');

// const clonedDiv = originalDiv.cloneNode(true);
// document.body.appendChild(clonedDiv);


// //task 3): Exercise 3: Remove a Specific Child Element
// // - **Task**: Select a specific <li> element from a list and remove it.
// // - **Methods**: removeChild.
// const list = document.getElementById('myList');

// const listItemToRemove = list.children[2]; 
// list.removeChild(listItemToRemove);


// //task 4):Exercise 4: Replace a Child Element
// // - **Task**: Replace an existing `<h1>` with a new `<h2>` element.
// // - **Methods**: `createElement`, `replaceChild`.
// const h1Element = document.querySelector('h1'); 
// const h2Element = document.createElement('h2');

// h2Element.textContent = 'This is a new heading';
// h1Element.parentNode.replaceChild(h2Element, h1Element);


// //task 5):Exercise 5: Remove an Element Directly
// // - **Task**: Select a paragraph element and remove it from the DOM.
// // - **Methods**: `remove`.
// const paragraph = document.querySelector('p'); 

// paragraph.remove();


