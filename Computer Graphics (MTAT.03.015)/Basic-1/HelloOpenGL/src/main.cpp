// ---------------------------- Includes -------------------------- //
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <GLFW/glfw3.h>
#include <math.h>

#define PI 3.14159265

// ---------------------------- Forward declarations -------------------------- //
void draw(GLFWwindow *win);
void drawTriangle(float x, float y);

// ---------------------------- Input -------------------------- //
// Listen for input event
static void key_callback(GLFWwindow* window, int key, int scancode, int action, int mods) {
    if (key == GLFW_KEY_ESCAPE && action == GLFW_PRESS)
        glfwSetWindowShouldClose(window, GL_TRUE);
}

// ---------------------------- Main -------------------------- //
int main(int argc, char *argv[]) {
    GLFWwindow *win;

    if (!glfwInit()) { //Something went wrong with GLFW initialization
        exit (EXIT_FAILURE);
    }

    win = glfwCreateWindow(640, 480, "Hello GLFW!", NULL, NULL);

    if (!win) {
        glfwTerminate();
        exit(EXIT_FAILURE);
    }

    //Sets the win context current in OpenGL state machine.
    //Following OpenGL commands will be directed at this context.
    glfwMakeContextCurrent(win);

    //Register the callback method for input
    glfwSetKeyCallback(win, key_callback);

    const GLubyte* renderer = glGetString (GL_RENDERER); // get renderer string
    const GLubyte* version = glGetString (GL_VERSION); // version as a string
    printf ("Renderer: %s\n", renderer);
    printf ("OpenGL version supported %s\n", version);

    //Event loop
    while (!glfwWindowShouldClose(win)) {
        draw(win);
        usleep(1000);
        glfwPollEvents();
    }

    glfwTerminate();
    exit(EXIT_SUCCESS);
    return 0;
}

// ---------------------------- Drawing -------------------------- //
/**
 * Everything related to drawing the scene
 */
void draw(GLFWwindow *win) {
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT); //Clear last frame

    drawTriangle(0.0f,0.0f);

    glfwSwapBuffers(win);
}
/**
 * --Task--
 * Find the correct coordinates and draw the equilateral triangle
 * In the older OpenGL there is a function glVertex*() to specify vertices.
 * See: https://www.opengl.org/sdk/docs/man2/xhtml/glVertex.xml
 */
void drawTriangle(float x, float y) {

    float size = 0.5;
    float height = size * (sqrt(3) / 2);
    //Draw triangle Way-1
//    glBegin (GL_TRIANGLES);
//        glColor3f (1.0, 0.0, 0.0); //set color
//        glVertex3f(x + (size/2.0) ,  y - (height / 2.0) , 0.0f);//left of window
//        glVertex3f(x - (size/2.0) ,  y - (height / 2.0) , 0.0f);//bottom of window
//        glVertex3f(x , y + (height / 2.0) , 0.0f);//right of window
//    glEnd ();




    float angle = (PI * 2)/3;
    //Draw triangle Way-2
    glBegin (GL_TRIANGLES);
        glColor3f (1.0, 0.0, 0.0); //set color
        glVertex3f((x + cos(angle) * size)/1.33 , y + sin(angle) * size  , 0.0);//left of window
        glVertex3f((x + cos(angle * 2) * size)/1.33 , y + sin(angle * 2) * size , 0.0);//bottom of window
        glVertex3f((x + cos(angle * 3) * size)/1.33 , y + sin(angle * 3) * size , 0.0);//right of window
    glEnd ();

}
