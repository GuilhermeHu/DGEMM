// Autor: Bernardo Pozzato


class Matrix {
    constructor(rows, cols, isRandom = false) {
        this.rows = rows;
        this.cols = cols;
        this.data = new Float64Array(rows * cols); // Usar Float64Array para melhorar o desempenho

        if (isRandom) {
            this.generateRandomData();
        }
    }

    generateRandomData() {
        for (let i = 0; i < this.rows * this.cols; i++) {
            this.data[i] = Math.random() * 10; // Números aleatórios de ponto flutuante entre 0 e 10
        }
    }

    get(row, col) {
        return this.data[row * this.cols + col];
    }

    set(row, col, value) {
        this.data[row * this.cols + col] = value;
    }

    static multiply(matrixA, matrixB) {
        const result = new Matrix(matrixA.rows, matrixB.cols);

        const aRows = matrixA.rows, aCols = matrixA.cols;
        const bCols = matrixB.cols;

        const aData = matrixA.data;
        const bData = matrixB.data;
        const cData = result.data;

        for (let i = 0; i < aRows; i++) {
            for (let j = 0; j < bCols; j++) {
                let sum = 0;
                for (let k = 0; k < aCols; k++) {
                    sum += aData[i * aCols + k] * bData[k * bCols + j];
                }
                cData[i * bCols + j] = sum;
            }
        }

        return result;
    }

    static measureExecutionTime(matrixA, matrixB) {
        const start = performance.now();
        Matrix.multiply(matrixA, matrixB);
        const end = performance.now();
        return (end - start) / 1000; // Converter milissegundos para segundos
    }
}

// Exemplo de uso
const rowsA = 8192; // Número de linhas da matriz A
const colsA = 8192;  // Número de colunas da matriz A
const rowsB = 8192;  // Número de linhas da matriz B
const colsB = 8192;  // Número de colunas da matriz B

const matrixA = new Matrix(rowsA, colsA, true);
const matrixB = new Matrix(rowsB, colsB, true);

try {
    const executionTime = Matrix.measureExecutionTime(matrixA, matrixB);
    console.log(Tempo de execução da multiplicação: ${executionTime.toFixed(10)} segundos);
} catch (error) {
    console.error(error.message);
}
