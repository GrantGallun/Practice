function getComputerChoice(){
    let choice = Math.floor(Math.random()*3+1);
    if (choice==1){
        return "rock";
    }
    if (choice==2){
        return "scissors";
    }
    if (choice==3){
        return "paper";
    }
}

function getPlayerSelection(){
    let keyboardsel=prompt("Rock Paper Scissors 1,2,3... (Enter Choice Here)");
    if (keyboardsel.toLowerCase()==="rock" || keyboardsel.toLowerCase()==="paper" || keyboardsel.toLowerCase()==="scissors"){
        return keyboardsel.toLowerCase()

    }
    else{
        getPlayerSelection()
    }
}

let pscore=0;
let cscore=0;
let playerSelection=getPlayerSelection();
let computerSelection=getComputerChoice();

function playRound(playerSelection, computerSelection){
 if (playerSelection=="rock" && computerSelection=="scissors"){
    console.log("You Win! Rock beats Scissors");
    pscore+=1;
 }
 else if (playerSelection=="paper" && computerSelection=="rock"){
    console.log("You Win! Paper beats Rock");
    pscore+=1;
 }
 else if (playerSelection=="scissors" && computerSelection=="paper"){
    console.log("You Win! Scissors beats Paper");
    pscore+=1;
 }


 else if (computerSelection=="rock" && playerSelection=="scissors"){
    console.log("You Lose! Rock beats Scissors");
    cscore+=1;
 }
 else if (computerSelection=="paper" && playerSelection=="rock"){
    console.log("You Lose! Paper beats Rock");
    cscore+=1;
 }
 else if (computerSelection=="scissors" && playerSelection=="paper"){
    console.log("You Lose! Scissors beats Paper");
    cscore+=1;
 }
 else{
    console.log("Its a Tie!");
 }

}

console.log(computerSelection);
console.log(playerSelection);
playRound(playerSelection,computerSelection)
while(pscore<3 && cscore<3){
    computerSelection=getComputerChoice();
    playerSelection=getPlayerSelection();
    playRound(playerSelection,computerSelection);
}
if(pscore>cscore){
    console.log("You beat the bot!")
}else{
    console.log("Better luck next time!")
}