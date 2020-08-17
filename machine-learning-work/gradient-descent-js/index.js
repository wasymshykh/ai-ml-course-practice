
const x = [1, 2, 3]
const y = [1.5, 2, 2.5]
let data = {
    'n': x.length,
    'w0': 0.5,
    'w1': 0.5,
    'learning_rate': 0.1,
    'iterations': 3
}

const gradient_descent_batch_method = ({n, w0, w1, learning_rate, iterations}) => {
    for (let iteration = 0; iteration < iterations; iteration++) {
        console.log(`iteration-> ${iteration+1} \t w0 -> {${w0}} \t w1 -> {${w1}}`)
        
        console.log(`X \t Y \t Yp \t Err`)
        let err = 0
        for (let i = 0; i < n; i++) {
            let yp = w0 + w1 * x[i]
            err += y[i] - yp
            console.log(`${x[i]} \t ${y[i]} \t ${yp.toFixed(3)} \t ${(y[i] - yp).toFixed(3)}`)
        }
        
        /* Summission part of equation */
        let w0sum = w1sum = 0
        for (let i = 0; i < n; i++) {
            w0sum += (y[i] - w0 - (w1*x[i]))
            w1sum += (y[i] - w0 - (w1*x[i]))*(x[i])
        }

        /* Combining everything in equation */
        w0 = w0 + (learning_rate * (2/n) * w0sum)
        w1 = w1 + (learning_rate * (2/n) * w1sum)
        
        console.log(`error-> ${err/n}\n`)
    }
}

gradient_descent_batch_method(data)

const gradient_descent_stochastic_method = ({n, w0, w1, learning_rate}) => {
    for (let iteration = 0; iteration < n; iteration++) {
        console.log(`iteration-> ${iteration+1} \t w0 -> {${w0}} \t w1 -> {${w1}}`)
        
        console.log(`X \t Y \t Yp \t Err`)
        let err = 0
        for (let i = 0; i < n; i++) {
            let yp = w0 + w1 * x[i]
            err += y[i] - yp
            console.log(`${x[i]} \t ${y[i]} \t ${yp.toFixed(3)} \t ${(y[i] - yp).toFixed(3)}`)
        }

        w0 = w0 + (learning_rate * (y[iteration] - w0 - (w1*x[iteration])))
        w1 = w1 + (learning_rate * (y[iteration] - w0 - (w1*x[iteration]))*(x[iteration]))
        
        console.log(`error-> ${err/n}\n`)
    }
}

gradient_descent_stochastic_method(data)
