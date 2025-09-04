import java.nio.file.{Files, Paths}
import scala.util.{Try, Using}

object Main {
  def main(args: Array[String]): Unit = {
    val filePath = "data6.txt"

    val lines = Using(scala.io.Source.fromFile(filePath)) { source =>
      source.getLines().toList
    }.getOrElse(List.empty)

    val outputLines = lines.zipWithIndex.map {
      case (line, 0) => s"$line,Comments" // header
      case (line, _) =>
        val parts = line.split(",")
        if (parts.length < 9) line // skip invalid lines
        else {
          val summary = parts(7).trim
          val evaluation: Float = Try(parts(8).toFloat).getOrElse(0f)

          val comments = (summary, evaluation) match {
            case ("super", e) if e >= 3 => "Excellent"
            case ("super", _)           => "Good but inconsistent"
            case (_, e) if e >= 2       => "Promising"
            case _                      => "Needs Improvement"
          }
          s"$line,$comments"
        }
    }

    Files.write(Paths.get("data7.txt"), outputLines.mkString("\n").getBytes)
  }
}