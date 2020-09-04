const actual = ['R', 'Y', 'B', 'B', 'Y', 'R', 'Y', 'G', 'G', 'B', 'R', 'Y', 'Y', 'Y', 'G']
const predicted = ['R', 'G', 'B', 'R', 'Y', 'R', 'Y', 'Y', 'R', 'B', 'R', 'Y', 'R', 'B', 'G']

class Confusion {

    constructor (actual, predicted) {
        this._validate_data(actual, predicted);
        this._actual = actual
        this._predicted = predicted
        this._classes = []
        this._extract_classes();
    }

    make_matrix () {
        console.log('🚀 Making empty confusion matrix....\n');
        this._confusion_matrix = [];
        for (let i = 0; i < this._classes.length; i++) {
            this._confusion_matrix.push([])
            for (let j = 0; j < this._classes.length; j++) {
                this._confusion_matrix[i].push(0);
            }
        }
        this.display_confusion_matrix();
    }

    populate_confusion_matrix () {
        console.log('🚀 Populating confusion matrix....\n');
        this._actual.forEach((actual, index) => {
            let predicted = this._predicted[index];
            this._confusion_matrix[this._classes.indexOf(predicted)][this._classes.indexOf(actual)] += 1
        });
        this.display_confusion_matrix()
    }

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

let o = new Confusion(actual, predicted)
o.make_matrix()
o.populate_confusion_matrix()