const axios = require("axios");
// axios
//   .get("https://cat-fact.herokuapp.com/facts/random")
//   .then((response) => console.log(response.data.text));

async function getToken(){
  const options = {headers: {'Content-Type': 'application/json', 'Accept': 'application/json'}};

  accessToken = await axios.post('https://tecweb-js.insper-comp.com.br/token', {username: "gabrielmt2"}, options).then((response) => {return(response.data.accessToken)});

  return accessToken
}

async function getExercises(){
  
}

async function main(){
  accessToken = await getToken();
  console.log(accessToken);
}

main()