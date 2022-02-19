# Virtual-Baymax

If you have watched the movie Big Hero 6, you are probably aware of the advantages of a personal healthcare assistant, and that their uses can be made limitless. This is especially in the case of individuals requiring special assistance such as differently-abled people and senior citizens. A personal healthcare assistant can provide immediate prognosis, tend to you, call the authorities and whatnot.

This project is similar but a very small step towards the cause.

The ideology of this project is to make an interactive platform that provides a medium of communication between a concerned user/patient and an AI that delivers accurate predictions for prognosis while taking into consideration the patients’ symptoms and various important details. ML approaches are then applied to devise a diagnosis. Most crucially, a WhatsApp bot will be developed as a platform for communication. As most Indian smartphone users have access to WhatsApp, making an easily accessible bot that one can simply text to identify their symptoms and plan of action for treatment would make the process easier. If this idea catches traction in the future, we could hope for implementations where the bot could call EMTs in case a serious situation arises or a home visit needs to be arranged.

Using ML approaches (Random Forest) to solve the classification problem - Whether an individual has diabetes, or not, we identify persons who are prone to the illness with an accuracy of 98.5%. This is achieved by first obtaining values of the data we need from the user. These values are obtained by means of the bot via user input. Second, these values are the untrained data that we predict the labels of the data values on the basis of the trained model. Third, the prediction is either 0 or 1. where 1 indicates a higher probability of the person either already having diabetes or being prone to it and 0 indicates that they are in the clear. Fourth, this prediction is then reported to the user via the bot.

The future of a system like this can cut costs, reduce the carbon footprint, deliver more accurate responses, and more. The advantages are limitless through innovation.
