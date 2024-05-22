// Autor: Bernardo Pozzato


class Matrix {
    constructor(rows, cols, isRandom = false) {
        this.rows = rows;
        this.cols = cols;
        this.data = Array.from({ length: rows }, () => Array(cols).fill(0));

        if (isRandom) {
            this.generateRandomData();
        }
    }

    generateRandomData() {
        for (let i = 0; i < this.rows; i++) {
            for (let j = 0; j < this.cols; j++) {
                this.data[i][j] = Math.random() * 10; // Números aleatórios de ponto flutuante entre 0 e 10
            }
        }
    }

    static multiply(matrixA, matrixB) {
        const result = new Matrix(matrixA.rows, matrixB.cols);

        for (let i = 0; i < matrixA.rows; i++) {
            for (let j = 0; j < matrixB.cols; j++) {
                let sum = 0;
                for (let k = 0; k < matrixA.cols; k++) {
                    sum += matrixA.data[i][k] * matrixB.data[k][j];
                }
                result.data[i][j] = sum;
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
const rowsA = 4096; // Número de linhas da matriz A
const colsA = 4096;  // Número de colunas da matriz A
const rowsB = 4096;  // Número de linhas da matriz B
const colsB = 4096;  // Número de colunas da matriz B

const matrixA = new Matrix(rowsA, colsA, true);
const matrixB = new Matrix(rowsB, colsB, true);

try {
    const executionTime = Matrix.measureExecutionTime(matrixA, matrixB);
    console.log(Tempo de execução da multiplicação: ${executionTime.toFixed(10)} segundos);
} catch (error) {
    console.error(error.message);
}
