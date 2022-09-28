var content;
var image;
var playerName;
var playerRace;
var playerClass;
var playerStrength;
var playerHealth;
var playerMagic;
var playerMoney;


window.onload = function()
{
    image = document.getElementById('imageForGame');
    image.innerHTML = "<img src='./images/cave.jpg' />";

    content = document.getElementById('content');
    content.innerHTML = "<h2> Welcome to the Cave!</h2> <p> Are you ready to try your hand in this adventure?</p>";
    content.innerHTML += "<button id='btnReady'>Ready!</button>";
    
    document.getElementById('btnReady').addEventListener('click', registration) ;
}

function registration(e)
{
    image.innerHTML = "<img src='./images/please-register.jpg' />";

    content.innerHTML = 
        `<h1>Hello!</h1>
        <p>Before you are able to enter the cave, you must do a quick registration process.</p>
        <p>Fill in the information below</p>
        
        <label for='name'>Name: </label>
            <input type='text'id='name' /> <br>
        <label for='race'>Race: </label>
            <input type='radio' name='race' id='fairy' value="Fairy">Fairy</input>
            <input type='radio' name='race' id='elf' value="Elf">Elf</input>
            <input type='radio' name='race' id='gnome' value="Gnome">Gnome</input> <br>
        <label for='class'>Class: </label>
            <input type='radio' name='class' id='warrior' value="Warrior">Warrior</input>
            <input type='radio' name='class' id='mage' value="Mage">Mage</input>
            <input type='radio' name='class' id='cleric' value="Cleric">Cleric</input> <br>
        <button id="btnRegister">Register</button>`
    ;

    playerName = document.getElementById("btnRegister").addEventListener('click', playerReg );
    
}

function playerReg(e)
{



    playerName = document.getElementById('name').value;
    
    if (document.getElementById('fairy').checked) {
        playerRace = document.getElementById('fairy').value;
        image.innerHTML = "<img src='./images/fairy.png' />";
    } else if (document.getElementById('elf').checked) {
        playerRace = document.getElementById('elf').value;
        image.innerHTML = "<img src='./images/elf.png' />";
    } else {
        playerRace = document.getElementById('gnome').value;
        image.innerHTML = "<img src='./images/gnome.png' />";
    }

    if (document.getElementById('warrior').checked) {
        playerClass = document.getElementById('warrior').value;
    } else if (document.getElementById('mage').checked) {
        playerClass = document.getElementById('mage').value;
    } else {
        playerClass = document.getElementById('cleric').value;
    }

    // base player attributes for strengths, health, and magic
    playerStrength = 5;
    playerHealth = 5;
    playerMagic = 5;
    playerMoney = 15;


    // fairy attributes
    if (playerRace =="Fairy")
    {
        playerStrength = playerStrength;
        playerHealth += 5;
        playerMagic += 10;
    }

    //elf attributes
    if (playerRace =="Elf")
    {
        playerStrength += 5;
        playerHealth += 10;
        playerMagic = playerMagic;
    }
    
    //gnome attributes
    if (playerRace =="Gnome")
    {
        playerStrength += 10;
        playerHealth = playerHealth;
        playerMagic += 5;
    }

    //mage attributes
    if (playerClass =="Mage")
    {
        playerStrength = playerStrength;
        playerHealth += 5;
        playerMagic += 10;
    }

    // cleric attributes
    if (playerClass =="Cleric")
    {
        playerStrength += 5;
        playerHealth += 10;
        playerMagic = playerMagic;
    }
    
    // warrior attributes
    if (playerClass =="Warrior")
    {
        playerStrength += 10;
        playerHealth = playerHealth;
        playerMagic += 5;
    }
       
    content.innerHTML = "Name: " + playerName + "<br>Race: " + playerRace + "<Br>Class: " + playerClass +"<br>Strength Level: " + playerStrength + "<br>Magic Level: " + playerMagic + "<br>Health Level: " + playerHealth; 
    content.innerHTML += 
        `
            <p> You are all registered. Before you go, look at what equipment we have. You may want something to help with your adventure.</p>
            <button id="btnStore">Review Equipment</button>
            <button id="btnStartCave">Head to the Cave</button>        
        `

    document.getElementById("btnStore").addEventListener('click', storeEquip );
    document.getElementById('btnStartCave').addEventListener('click', finalReg );

}

function storeEquip(e)
{
    image.innerHTML = "<img src='./images/swordshield.png' />";

    content.innerHTML = 
    `
    <h1> Equipment Rentals </h1>
    <p> Check out the various equipment you can rent. Prices and equipment detail are provided. Select which items you would like and let me know when you are done.<p>
    <p><strong> Your Wallet: `+playerMoney+` coins </strong>
    <table>
        <tr>
            <th>Item</th>
            <th>Price</th>
            <th>Description</th>
            <th></th>
        </tr>
        <tr>
            <td>Sword</td>
            <td>5 coins</td>
            <td>Increases Strength 5 points</td>
            <td><input type="checkbox" id="sword" name="sword" value="5"></td>
        </tr>
        <tr>
            <td>Dragon Heart</td>
            <td>10 coins</td>
            <td>Increases Health 10 points</td>
            <td><input type="checkbox" id="dragonHeart" name="dragonHeart" value="10"></td>
        </tr>
        <tr>
            <td>Witches Hat</td>
            <td>5 coins</td>
            <td>Increases Magic 8 points</td>
            <td><input type="checkbox" id="witchHat" name="witchHat" value="8"></td>
        </tr>
    </table>
    <button id="btnPurchase">Checkout</button>
    ` ;
    
    document.getElementById('btnPurchase').addEventListener('click', storePurchase);
}
  
function storePurchase()
{
    var sword = 0;
    var heart = 0;
    var hat = 0;

    // image.innerHTML = "<img src='./images/swordshield.png' />";
    image.innerHTML = "";


    if(document.getElementById("sword").checked)
    {
        sword = 5;
    }
    if(document.getElementById("dragonHeart").checked)
    {
        heart = 10;
    }
    if(document.getElementById("witchHat").checked)
    {
        hat = 8;
    }
    
    var expense = (sword + heart + hat);

    if (playerMoney >= expense ) 
    {
        playerStrength += sword;
        playerHealth += heart;
        playerMagic += hat;
        
        content.innerHTML = `Perfect. Let's checkout your updated Stats.<br>
        <button id="statsUpdate">Next</button>`;
        
        document.getElementById("statsUpdate").addEventListener('click', playerStats);

    } else
    {
        alert("You don't have enought money for all that. Try again.");

    }
}

function playerStats(e)
{
    // image.innerHTML = "<img src='./images/swordshield.png' />";
    image.innerHTML = "";

    content.innerHTML = 
    `Name: ` + playerName + 
    `<br>Race: ` + playerRace + 
    `<br>Class: ` + playerClass + 
    `<br>Strength: ` + playerStrength +
    `<br>Magic: ` + playerMagic + 
    `<br>Health: ` + playerHealth +
    `<br><button id="next">Continue</button>`;

    document.getElementById("next").addEventListener('click', finalReg);

}

function finalReg(e)
{
    // image.innerHTML = "<img src='./images/swordshield.png' />";
    image.innerHTML = "";

    content.innerHTML = `<p>Good luck on your adventure!</p><button id="scene1">Enter Cave</button>`
    document.getElementById("scene1").addEventListener('click', scene1);
}

function scene1(e)
{
    // image.innerHTML = "<img src='./images/swordshield.png' />";
    image.innerHTML = "";

    content.innerHTML = `
        <p>It is dark and the only light is the torch you just recieved from the Registrar.
		<br>You can see about 15 feet away.
		<br>The stone walls are wet and damp. The air smells like a someone forgot to flush the toilet.
		<br>You come up to a wall.
		<br>You are able to continue to either the left or the right.</p>
		
		<p>What direction do you take?</p>
		<button id="left">Left</button> or <button id="right">Right</button>
    `;
    
    document.getElementById("left").addEventListener('click', scene2);
    document.getElementById("right").addEventListener('click', scene3);
}

function scene2(e)
{
    // image.innerHTML = "<img src='./images/swordshield.png' />";
    image.innerHTML = "";

    content.innerHTML=`
    <p>Well the smell hasn't gotten worse, but this hall looks like it might be smaller then the other one.
	<br>As you continue walking, you see light in the distance.
	<br>You notice that there is a bend in the hall.
	<br>You are almost to the end of the hall and you see a door.
	<br>But there is an aweful smell coming from the room.
	<br>The only way to know what the smell is, is to enter the room. </p>
	<button id="next">Continue through the door...</button>
    `;
    document.getElementById("next").addEventListener('click', scene4);

}

function scene3(e)
{
    // image.innerHTML = "<img src='./images/swordshield.png' />";
    image.innerHTML = "";

    content.innerHTML=`
    <p>They walk a short distance down this hall when all of a sudden....</p>
	<p>*SMASH*</p>
	<p>The ceiling has caved in. The whole hall is covered to the top with debris.
    <br>Do you attempt to dig a path through the debris or return the other way down the hall?</p>
	<button id="dig">Dig!</button> or <button id="turnAround">Yea...turning around</button>
	`;
	
    document.getElementById("dig").addEventListener('click', scene18);
    document.getElementById("turnAround").addEventListener('click', scene2);

}

function scene4(e)
{
    // image.innerHTML = "<img src='./images/swordshield.png' />";
    image.innerHTML = "";

    content.innerHTML = `
    <p>The source of the smell is definitly here.
    <br>You take the torch and lights up the room torches near the door.
    <br>As the room light, you can see bones all over the floor. Something shifts in the corner.</p>
    <p>A low growl comes from the figure and it starts to rise up. It turns around. An ogre.</p>
    <p>Do you try to fight or run away?</p>
	<button id="fight">FIGHT!</button> or <button id="runAway">RUN!</button>
	`;
	
    document.getElementById("fight").addEventListener('click', combat1);
    document.getElementById("runAway").addEventListener('click', run1);

}

function scene5(e)
{
    // image.innerHTML = "<img src='./images/swordshield.png' />";
    image.innerHTML = "";

    content.innerHTML = `
    <p>The ogre is dead. You made it out...mostly alive.
    <br>As you look around the room, you notice a door in the back.
    <br>Finally - a way out!</p>
	<button id="next">Continue...</button>
    `;
    document.getElementById("next").addEventListener('click', scene6);
}

function scene6(e)
{
    // image.innerHTML = "<img src='./images/swordshield.png' />";
    image.innerHTML = "";

    content.innerHTML = `
    <p>Finally out of the room , you notice a doorway to the right in the hall.
    <br>Do you continue down the hallway or go through the door?</p>

	<button id="hall">No more unknown doorways...</button> or <button id="door">Let's try Room #2</button>
    `;
    document.getElementById("hall").addEventListener('click', scene8);
    document.getElementById("door").addEventListener('click', scene7);
}


function scene7(e)
{
    // image.innerHTML = "<img src='./images/swordshield.png' />";
    image.innerHTML = "";

    playerMoney += 25;
    
    content.innerHTML = `
    <p>This room is empty except for a box in the back of the room.
    <br>You walk to the back of the room, open the box, and find....</p>
    
    Coins!
    
    <p>Well this will help pay for any equipment rental fees...</p>
    Coin Purse: ` + playerMoney + `
	<br><button id="returnHall">Return to the hall</button>
    `;
    document.getElementById("returnHall").addEventListener('click', scene8);
}

function scene8(e)
{
    // image.innerHTML = "<img src='./images/swordshield.png' />";
    image.innerHTML = "";

  content.innerHTML = `
    <p>This hallway feels like it takes forever.
    <br>After walking for who knows how long, you finally reach the end of the hall. 
    <br>There are two doors.</p>
    <p>In front of the doors, there is a troll standing guard.</p>
    <p>*TROLL*:  Welcome to the end. There are two choices you are able to take. 
    <br>Everyone is free to pass through the door on the right, but you will have a final battle to come.
    <br>Or for a fee, you can pass through the door on the left. You will have completed the cave and win.
    <br>The fee is <strong>20 coins</strong>.</p>
    What will you decide?
    <br><button id="freedom">Pay and turn Left</button> or <button id="finalBoss">Right and Fight!</button>
    `;
    document.getElementById("freedom").addEventListener('click', function(){
        if (playerMoney >= 20)
        {
            content.innerHTML =`<br>Thank you for your business. You can go on through.
            <br><button id="paid">Continue...</button>`
            document.getElementById("paid").addEventListener('click', finalWin);
        }
        else
        {
            content.innerHTML =`<br>Sorry, that isn't enough money.
            <br><button id="turnRight">Right and fight...I guess...</button>`
            document.getElementById("turnRight").addEventListener('click', finalCombat);
        }
        
    });
    document.getElementById("finalBoss").addEventListener('click', finalCombat);
}


function combat1(e)
{
    // image.innerHTML = "<img src='./images/swordshield.png' />";
    image.innerHTML = "";

    var monsterHealth = 10;
    var monsterStrength = 3;

    content.innerHTML=`
    <p>Get ready and FIGHT!</p>
    <button id="attack">Attack!</button>`;
    
    document.getElementById("attack").addEventListener('click', function() {

        if (playerStrength >= monsterHealth || (playerStrength + playerMagic) >= (monsterStrength + monsterHealth) )
        {
            content.innerHTML +=`<br> <p>The ogre stops attacking.</p>
            <br><button id="next">Continue...</button>`;
            document.getElementById("next").addEventListener('click', scene5);
        }
        else
        {
            content.innerHTML +=`The ogre killed you. Do you want to reincarnate and try again?
            <button id="retry">Reincarnate</button> or <button id="death">Sleep Forever More</button>`;
            document.getElementById("retry").addEventListener('click', retry);
            document.getElementById("death").addEventListener('click', death);
        }
    });
}

function finalCombat(e)
{
    // image.innerHTML = "<img src='./images/swordshield.png' />";
    image.innerHTML = "";

    content.innerHTML=`
    <p>As soon as you walked into the room, a loud grumble came from the far side. 
    <br>Suddenly the ground shook almost like an earthquake. 
    <br>From where the grumble came, a figure started to move and grow...
    <br>It got larger and larger and more clear</p>
    <p>A DRAGON!</p>
    <p>*DRAGON*: "Dinner time I see. You smell delicious."</p>
    <p>The dragon was so swift, you are incased in utter darkness.
    <br>It feels like you were dropped into a lake.
    <br>You feel around and you grab onto something...its a skull.
    <br>The liquid starts to burn.</p>
    
    <p>The dragon ate you. You are dead. Want to try again after your reincarnation or stay in the otherworld?</p>
    <button id="retry">Reincarnate</button> or <button id="death">Sleep Forever More</button>
    `;
    document.getElementById("retry").addEventListener('click', retry);
    document.getElementById("death").addEventListener('click', death);
    
}

function run1(e)
{
    // image.innerHTML = "<img src='./images/swordshield.png' />";
    image.innerHTML = "";

   content.innerHTML = `
   <p>You all run to the door that you came in, however, the door shut behind you.
	<br>The door is locked. </p>

	<p>Well...this is awkward. Guess there wasn't a choice. You need to fight.</p>
	<br><button id="fight">FIGHT!</button>
   ` ;
    document.getElementById("fight").addEventListener('click', combat1);
}

function retry(e)
{
   location.reload(); 
}

function death(e)
{
   window.close(); 
}

function finalWin(e)
{
    // image.innerHTML = "<img src='./images/swordshield.png' />";
    image.innerHTML = "";

   content.innerHTML=`<p>You won! Congrats!
    </p>
    <p>Thanks for playing this mini text adventure game!</p>
    <button id="close">Close</button>
    `;
    document.getElementById("close").addEventListener('click', death);
}


function scene18(e)
{
    // image.innerHTML = "<img src='./images/swordshield.png' />";
    image.innerHTML = "";

    content.innerHTML=`
    <p>You try to get the debris out of the way.
	<br>Every time they move a little, a lot more falls in it's place.
	<br>Time to give up on the digging this time, let's return down the other hall.</p>
	<button id="next">Time to turn around</button>
    `;
    document.getElementById("next").addEventListener('click', scene2);
}
