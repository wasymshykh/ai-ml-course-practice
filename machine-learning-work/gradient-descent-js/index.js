
const x = [1, 2, 3]
const y = [1.5, 2, 2.5]

let n = x.length

let w0 = 0.5
let w1 = 0.5
let learning_rate = 0.1
let iterations = 3

const gradient_descent_batch_method = () => {
    for (let iteration = 0; iteration < iterations; iteration++) {
        console.log(`iteration-> ${iteration+1} \t w0 -> {${w0}} \t w1 -> {${w1}}`);
        
        console.log(`X \t Y \t Yp \t Err`);
        err = 0;
        for (let i = 0; i < n; i++) {
            yp = w0 + w1 * x[i];
            err += y[i] - yp;
            console.log(`${x[i]} \t ${y[i]} \t ${yp.toFixed(3)} \t ${(y[i] - yp).toFixed(3)}`);
        }
        
        /* Summission part of equation */
        let w0sum = 0;
        let w1sum = 0;
        for (let i = 0; i < n; i++) {
            w0sum += (y[i] - w0 - (w1*x[i]))
            w1sum += (y[i] - w0 - (w1*x[i]))*(x[i])
        }

        /* Combining everything in equation */
        w0 = w0 + (learning_rate * (2/n) * w0sum);
        w1 = w1 + (learning_rate * (2/n) * w1sum);
        
        console.log(`error-> ${err/n}\n`);
    }
}

// gradient_descent_batch_method()



const gradient_descent_stochastic_method = () => {
    
    for (let iteration = 0; iteration < n; iteration++) {
        console.log(`iteration-> ${iteration+1} \t w0 -> {${w0}} \t w1 -> {${w1}}`);
        
        console.log(`X \t Y \t Yp \t Err`);
        err = 0;
        for (let i = 0; i < n; i++) {
            yp = w0 + w1 * x[i];
            err += y[i] - yp;
            console.log(`${x[i]} \t ${y[i]} \t ${yp.toFixed(3)} \t ${(y[i] - yp).toFixed(3)}`);
        }
        
        let w0sum = (y[iteration] - w0 - (w1*x[iteration]))
        let w1sum = (y[iteration] - w0 - (w1*x[iteration]))*(x[iteration])
        
        w0 = w0 + (learning_rate * w0sum);
        w1 = w1 + (learning_rate * w1sum);
        
        console.log(`error-> ${err/n}\n`);
    }

    
}

gradient_descent_stochastic_method();

