// Autor: Bernardo Pozzato

import Foundation
import Accelerate

func multiplyMatrices(_ matrixA: [[Double]], _ matrixB: [[Double]]) -> [[Double]]? {
    guard matrixA[0].count == matrixB.count else {
        return nil
    }
    
    let rowsA = matrixA.count
    let colsA = matrixA[0].count
    let rowsB = matrixB.count
    let colsB = matrixB[0].count
    
    var result = Array(repeating: Array(repeating: 0.0, count: colsB), count: rowsA)
    
    var matrixAFlat = matrixA.flatMap { $0 }
    var matrixBFlat = matrixB.flatMap { $0 }
    var resultFlat = Array(repeating: 0.0, count: rowsA * colsB)
    
    vDSP_mmulD(matrixAFlat, 1, matrixBFlat, 1, &resultFlat, 1, vDSP_Length(rowsA), vDSP_Length(colsB), vDSP_Length(colsA))
    
    var currentIndex = 0
    for i in 0..<rowsA {
        for j in 0..<colsB {
            result[i][j] = resultFlat[currentIndex]
            currentIndex += 1
        }
    }
    
    return result
}

func randomDoubleMatrix(size: Int) -> [[Double]] {
    var matrix = [[Double]]()
    
    for _ in 0..<size {
        var row = [Double]()
        for _ in 0..<size {
            row.append(Double.random(in: 0.000...1000.000))
        }
        matrix.append(row)
    }
    
    return matrix
}

let size = 16192
let matrixA = randomDoubleMatrix(size: size)
let matrixB = randomDoubleMatrix(size: size)

let startTime = Date()

if let result = multiplyMatrices(matrixA, matrixB) {
    let endTime = Date()
    let executionTime = endTime.timeIntervalSince(startTime)
    
    print("Tempo de execução: \(executionTime) segundos")
}
