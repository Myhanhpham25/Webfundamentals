var bob = "bob";
console.log(bob);


//++i before increment the i value before it console.log
//while loop 

//for loop on object 

var bob = {
	'a' : 1,
	'b' : 2,
	'c' : 3,
}

for (var key in bob){
	console.log (key); 
}

console.log (object.keys (bob));

//function are oject. 

function bob(){
	console.log ('hello world');
}
bob(); 

//called bob after bob wad defined. but in JS defined bob can be first bc JS pre run the 
//functions.

//parameter 

//return 

function bobmaker (name){
	var obj = {
		'name' : name,
		'greeting': function (){
			console.log ('Hi, My name is ' + name);
		}
	}
	return obj;
}
bobmaker ('Alan');

console.log (bobmaker('Alan')); //will return name + greeting

//=======
for (var i = 0; i <stuff.length; i++){ 
	var person = stuff[i];
	console.log (person);
for (var key in person) { //look for a person in the obejct, 
console.log (key); 
	}
}

//to split the array
for (var g = 0; g < person.curveball.length; g++) //object person, gives an array and grab the array length 
	console.log(person.curveball[g]); //give the array separately




