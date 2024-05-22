// Autor: Bernardo Pozzato

import Foundation

func multiplyMatrices(_ matrixA: [[Double]], _ matrixB: [[Double]]) -> [[Double]]? {
    var result = Array(repeating: Array(repeating: 0.0, count: matrixB[0].count), count: matrixA.count)
    
    for i in 0..<matrixA.count {
        for j in 0..<matrixB[0].count {
            for k in 0..<matrixB.count {
                result[i][j] += matrixA[i][k] * matrixB[k][j]
            }
        }
    }
    
    return result
}

func randomDoubleMatrix(size: Int) -> [[Double]] {
    var matrix = [[Double]]()
    
    for _ in 0..<size {
        var row = [Double]()
        for _ in 0..<size {
            row.append(Double.random(in: 0.0...1.0)) //
        }
        matrix.append(row)
    }
    
    return matrix
}

let size = 8192
let matrixA = randomDoubleMatrix(size: size)
let matrixB = randomDoubleMatrix(size: size)

let startTime = Date()

if let result = multiplyMatrices(matrixA, matrixB) {
    let endTime = Date()
    let executionTime = endTime.timeIntervalSince(startTime)
    
    print("Tempo de execução: \(executionTime) segundos")
}
