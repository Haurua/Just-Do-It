# Just-Do-It

The rite of passage for any and all aspiring developers, the to-do application. A web-application boasting the essential CRUD functionality and an eccentric visual design.

All views inherit from the Django View class with POST and GET methods being explicitly defined so that the logic of the CRUD operations are demonstrated concisely. Custom tags were used for string formatting and a lot of Django templating language was implemented for a more dynamical design.

Being a commonly suggested project, it was important to develop it to demonstrate that Django MVT and HTTP methods are understood.

# In-Depth Details

During development, I realised that there were some limitations with HTML, in this case it was with form elements. Whether submitted with a button or input element, they are required to be inside the form, introducing design limitations.

Wanting to overcome this, I used JavaScript; which allowed me to submit a form with any element in the document, by giving elements an on-click attribute that triggers a JavaScript function that submits the form. I ensured that the form still complies with the HTML5 validation and provided some pop-up confirmations before any edit/delete commands were carried out.

I wanted to demonstrate to myself that despite being more experienced with Python, I can apply my knowledge of programming fundamentals to achieve a simple task, even in a different language.
