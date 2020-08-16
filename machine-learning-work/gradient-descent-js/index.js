
const x = [1, 2, 3]
const y = [1.5, 2, 2.5]

let n = x.length

let w0 = 0.5
let w1 = 0.5
let learning_rate = 0.1
let error_tolerance = 0.1
let iterations = 3

console.log(`X \t Y \t Yp \t Err`);


for (let iteration = 0; iteration < iterations; iteration++) {

    err = 0;
    for (let i = 0; i < n; i++) {
        yp = w0 + w1 * x[i];
        err += y[i] - yp;
        console.log(`${x[i]} \t ${y[i]} \t ${yp} \t ${y[i] - yp}`);
    }

    w0output = `${w0.toFixed(5)} + (${learning_rate} x (2/${n}) x (`;

    w1output = `${w1.toFixed(5)} + (${learning_rate} x (2/${n}) x (`;

    let w0sum = 0;
    let w1sum = 0;
    for (let i = 0; i < n; i++) {
        w0sum += (y[i] - w0 - (w1*x[i]))
        w0output += ` (${y[i]} - ${w0.toFixed(5)} - (${w1.toFixed(5)} x ${x[i]})) +`
        
        w1sum += (y[i] - w0 - (w1*x[i]))*(x[i])
        w1output += ` (${y[i]} - ${w0.toFixed(5)} - (${w1.toFixed(5)} x ${x[i]})) x ${x[i]}) +`
    }
    
    w0output += `) )`;

    console.log("w0-> ", w0output);
    console.log("w1-> ", w1output);

    w0 = w0 + (learning_rate * (2/n) * w0sum);
    w1 = w1 + (learning_rate * (2/n) * w1sum);
    
    // if(Math.abs(err/n) < error_tolerance) {
        console.log('err->', err/n);
        console.log(`i-> ${iteration+1} w0 -> {${w0}} and w1 -> {${w1}}`);
        // break;
    // }
    console.log('-----------------------------------------------');
}


