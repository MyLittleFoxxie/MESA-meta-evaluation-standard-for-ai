import PDFKit
import Foundation
let args = CommandLine.arguments
let doc = PDFDocument(url: URL(fileURLWithPath: args[1]))!
var out = ""
for i in 0..<doc.pageCount { out += "=== PAGE \(i+1) ===\n" + (doc.page(at: i)?.string ?? "") + "\n" }
try! out.write(toFile: args[2], atomically: true, encoding: .utf8)
