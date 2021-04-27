const axios = require("axios");
// axios
//   .get("https://cat-fact.herokuapp.com/facts/random")
//   .then((response) => console.log(response.data.text));

async function getToken(){
  const options = {headers: {'Content-Type': 'application/json', 'Accept': 'application/json'}};

  const accessToken = await axios.post('https://tecweb-js.insper-comp.com.br/token', {username: "gabrielmt2"}, options).then((response) => {return(response.data.accessToken)});

  return accessToken
}

async function getExercises(accessToken){
  const options = {headers: {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': `Bearer ${accessToken}`}};

  const exercise = await axios.get('https://tecweb-js.insper-comp.com.br/exercicio', options).then((response) => {return(response.data)});

  return exercise
}

async function get(slug){
  const accessToken = await getToken();
  console.log(`Access token: ${accessToken}`);

  const exercise = await getExercises(accessToken)
  console.log(exercise);
}

async function post(accessToken, slug, resp){
  const options = {headers: {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': `Bearer ${accessToken}`}};

  const bool = await axios.post(`https://tecweb-js.insper-comp.com.br/${slug}`, {'resposta': resp}, options).then((response) => {return(response.data.sucesso)});

  return bool
}

async function soma(a, b){
  return ['soma', a+b];
}

async function tamanhostring(string){
  return ['tamanho-string', string.length];
}

async function nomedousuario(string){
  return ['nome-do-usuario', string.slice(0, string.indexOf('@'))];
}

async function jacawars(v, theta, g=9.8, d=100, r=2){
  const theta2 = theta * (180 / Math.PI);
  const dist = v**2 * Math.sin(2*theta2)/g;
  if (dist <= d-r){
    const resp = -1;
  }
  else if (dist >= d-r){
    const resp = 1;
  }
  else {
    const resp = 0;
  }

  return ['jaca-wars', resp];
}

async function anobissexto(ano){
  if (ano % 4 == 0){
    if (ano % 100 == 0){
      if (ano % 400 == 0){
        const resp = true;
      }
      else{
        const resp = false;
      }
    }
    else{
      const resp = true;
    }
  }
  else{
    const resp = false;
  }
  return ['ano-bissexto', resp];
}

async function volumedapizza(z, a){
  const v=Math.PI*(z**2)*a
  return ['volume-da-pizza', v]
}

async function mru(s0, v, t){
  const s=s0+v*t
  return ['mru', s]
}

async function invertestring(string){
  const split=string.split("");
  const reverse=split.reverse();
  const join=reverse.join("");

  return ['inverte-string', join]
}

async function somavalores(objeto){
  abcdef
  return ['soma-valores', objeto]
}

async function nesimoprimo(n){
    var array = [], upperLimit = Math.sqrt(10*n**2), output = [];

    for (var i = 0; i < n; i++) {
        array.push(true);
    }

    for (var i = 2; i <= upperLimit; i++) {
        if (array[i]) {
            for (var j = i * i; j < n; j += i) {
                array[j] = false;
            }
        }
    }

    for (var i = 2; i < n; i++) {
        if(array[i]) {
            output.push(i);
        }
    }

    return ['n-esimo-primo', output[n]]
}

async function maiorprefixocomum(string){
  av
  return ['maior-prefixo-comum', resp]
}

async function somapipipi(array){
  const menor = Math.min.apply(Math, array)
  const max = Math.max.apply(null, array);
  arr.splice(arr.indexOf(max), 1);
  const maior = Math.max.apply(null, arr);
  const resp = menor + maior
  return ['soma-segundo-maior-e-menor-numeros', resp]
}

get()