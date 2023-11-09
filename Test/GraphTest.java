import org.graphstream.graph.Graph;
import org.graphstream.graph.implementations.SingleGraph;
import org.graphstream.ui.spriteManager.*;
import java.lang.Thread;

public class GraphTest {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("org.graphstream.ui", "swing");
        Graph graph = new SingleGraph("Tutorial 1");

        graph.addNode("A");
        graph.addNode("B");
        graph.addNode("C");
        graph.addEdge("AB", "A", "B");
        graph.addEdge("BC", "B", "C");
        graph.addEdge("CA", "C", "A");

        SpriteManager sman = new SpriteManager(graph);
        Sprite s = sman.addSprite("S1");
        s.setPosition(2, 1, 0);
        s.attachToEdge("AB");
        graph.display();
        for(double i = 0; i < 1; i += 0.1){
            s.setPosition(i);
            Thread.sleep(500);
        }
    }
}