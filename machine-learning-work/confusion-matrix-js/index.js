class Confusion {
    /**
     * 
     * Description: Validates data in parameter, populates class variables and extract classes from arrays
     * @param {Array}   actual
     * @param {Array}   predicted
     * 
    **/
    constructor (actual, predicted) {
        this._validate_data(actual, predicted);
        this._actual = actual
        this._predicted = predicted
        this._classes = []
        this._extract_classes()
    }

    /**
     * 
     * Description: Creates an empty confusion matrix array w.r.t number of classes available
     * @param {boolean}   display
     * 
    **/
    make_matrix (display = false) {
        console.log('🚀 Making empty confusion matrix....\n');
        this._confusion_matrix = [];
        for (let i = 0; i < this._classes.length; i++) {
            this._confusion_matrix.push([])
            for (let j = 0; j < this._classes.length; j++) {
                this._confusion_matrix[i].push(0);
            }
        }
        if (display) {
            this.display_confusion_matrix();
        }
    }

    /**
     * 
     * Description: Populates the confusion matrix array w.r.t actual and predicted values
     * @param {boolean}   display
     * 
    **/
    populate_confusion_matrix (display = false) {
        console.log('🚀 Populating confusion matrix....\n');
        this._actual.forEach((actual, index) => {
            let predicted = this._predicted[index];
            this._confusion_matrix[this._classes.indexOf(predicted)][this._classes.indexOf(actual)] += 1
        })
        if (display) {
            this.display_confusion_matrix()
        }
    }

    /**
     * 
     * Description: Calculates presion and recall from confusion matrix data
     * 
    **/
    calculate_precision_recall () {
        
        for (let i = 0; i < this._classes.length; i++) {
            console.log('Calculating for ' + this._classes[i]);
            let [TP, FP, FN, TN] = [0, 0, 0, 0];

            for (let row = 0; row < this._confusion_matrix.length; row++) {
                for (let column = 0; column < this._confusion_matrix[row].length; column++) {
                    if (row == i && column == i) {
                        TP = this._confusion_matrix[row][column]
                    }
                    else if (row == i) {
                        FP += this._confusion_matrix[row][column]
                    }
                    else if (column == i) {
                        FN += this._confusion_matrix[row][column]
                    } else {
                        TN += this._confusion_matrix[row][column]
                    }
                }
            }

            let precision = TP/(TP + FP)
            let recall = TP/(TP + FN)

            console.log(' Precision: ' + precision.toFixed(3) + ' (' + (precision * 100).toFixed(1) + '%)')
            console.log(' Recall: ' + recall.toFixed(3) + '(' + (recall * 100).toFixed(1) + '%)\n')
        }

    }

    /**
     * 
     * Description: Print confusion matrix to console
     * 
    **/
    display_confusion_matrix () {
        let str = ''
        // header
        str += ' '.repeat((this._classes.length*2)+12) + 'actual\n'
        str += ' '.repeat(14) + '| ';
        this._classes.forEach(el => {
            str += el + ' | '
        });
        str += '\n' + ' '.repeat(10) + '-'.repeat(((this._classes.length+1)*4)+1) +'\n'

        // body
        this._classes.forEach((el, index) => {
            if (index+1 == (this._classes.length/2).toFixed(0)) {
                str += 'predicted'
            } else {
                str += ' '.repeat(9)
            }
            str += ' | ' + el + ' | '
            for (let i = 0; i < this._confusion_matrix[index].length; i++) {
                str += this._confusion_matrix[index][i] + ' | '
            }
            str += '\n'
        })

        // print
        console.log(str)
    }
 
    /**
     * 
     * Description: Extract all the classes from actual and predicted data
     * 
    **/
    _extract_classes () {
        this._actual.forEach((el, index) => {
            if (!this._classes.includes(el)) {
                this._classes.push(el)
            }
            if (!this._classes.includes(this._predicted[index])) {
                this._classes.push(this._predicted[index])
            }
        });
    }

    /**
     * 
     * Description: Validate given data checks for variable type and length 
     * 
    **/
    _validate_data (actual, predicted) {
        if (typeof actual === 'undefined' || typeof predicted === 'undefined') {
            console.log('❌ Err!!! Actual and Predicted parameters are required....\n');
            throw "Actual and Predicted parameters are required"
        }
        if (!Array.isArray(actual) || !Array.isArray(predicted)) {
            console.log('❌ Err!!! Parameters must be arrays....\n');
            throw "Parameters must be arrays"
        }
        if (actual.length !== predicted.length) {
            console.log('❌ Err!!! Actual and Predicted must be of same length....\n');
            throw "Actual and Predicted must be of same length"
        }
    }
}

const actual = ['R', 'Y', 'B', 'B', 'Y', 'R', 'Y', 'G', 'G', 'B', 'R', 'Y', 'Y', 'Y', 'G']
const predicted = ['R', 'G', 'B', 'R', 'Y', 'R', 'Y', 'Y', 'R', 'B', 'R', 'Y', 'R', 'B', 'G']

// const actual = ['T', 'T', 'T', 'F', 'F', 'T', 'F', 'T', 'T', 'F', 'T', 'T', 'F', 'F', 'T']
// const predicted = ['T', 'F', 'F', 'F', 'F', 'T', 'F', 'T', 'F', 'F', 'F', 'T', 'T', 'F', 'T']

let o = new Confusion(actual, predicted)
o.make_matrix()
o.populate_confusion_matrix(true)
o.calculate_precision_recall()
