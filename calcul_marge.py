def marge_enseigne(montant:float, y_pred:int, y_true:int) -> float:
    """
    Fonction qui défini la marge générée par l'enseigne selon
    le montant de la transaction bancaire (montant) et la nature de la prédiction du modèle
    Elle est utilisée pour évaluer la performance du modèle de scoring"""
    
    taux_marge_r = 0.05

    # Cas où on accepte une bonne transaction (TN - True Negative)
    if (y_pred==0 and y_true==0):
        marge = taux_marge_r*montant
    
    # Cas où on accepte une mauvaise transaction (FN - False Negative)
    elif (y_pred==0 and y_true==1):
        if montant<=20:
            marge = 0
        elif (montant>20 and montant<=50):
            marge = -0.2*montant
        elif (montant>50 and montant<=100):
            marge = -0.3*montant
        elif (montant>100 and montant<=200):
            marge = -0.5*montant
        elif (montant>200):
            marge = -0.8*montant
    
    # Cas où on refuse une bonne transaction (FP - False Positive)
    elif (y_pred==1 and y_true==0):
        marge = 0.7*montant*taux_marge_r
    
    # Cas où on refuse une transaction frauduleuse (TP - True Positive)
    elif (y_pred==1 and y_true==1):
        marge = 0

    return marge