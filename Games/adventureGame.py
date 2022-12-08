def questX():
  print("")

def questY():
  print("")

def beatenFigure():
  print("## FIGURE GIVES YOU ITEM ##")
  print("##SENDS YOU ON QUEST Y ##")
  questY()

def talkBartender():
  print("##SENDS YOU ON QUEST X ##")
  questX()


def holeOption(cupboard):
  choice = ""
  print("")
  print(
    "You fall after falling for what seems like forever, and land in a water-like spring."
  )
  print(
    "You walk on and on through the dark area, light caught by the clouds.")
  print(
    "On the ground, you spy two different objects that you may be able to use to light your path. One looks like a sort of red tube, maybe a flare, and the other a brown stick-like thing."
  )
  print("")
  choice = input(
    "Do you pick up the brown stick or the red tube to light your way?")
  print("")
  if choice == "red tube" or choice == "Red tube" or choice == "Pick up the red tube" or choice == "pick up the red tube":
    print(
      "You pick up the flare, and light the end. The room around you illuminates somewhat, revealing the tunnel ahead. You look back down at the flare, and immediately notice a word on the side, in bold black letters."
    )
    print("DYNAMITE")
    print(
      "Before you can react, the fuse reaches the end, and the last thing you hear is a deafening boom."
    )
    print("This is the end of your journey. Better luck next time.")
  if choice == "stick" or choice == "Stick" or choice == "pick up the brown stick" or choice == "Pick up the brown stick" or choice == "pick up the stick" or choice == "Pick up the brown stick":
    print("")
    print(
      "You pick up the stick and light then end. It makes a handy torch, and is very bright. You look back down at the flare on the floor, only to realise it is a stick of dynamite. Without trying to think about how you nearly met your demise, you pick up the dynamite and place it into your pocket, thinking it may become useful later."
    )
    print("")
    print(
      "You begin walking down the tunnel, the torch lighting our way. After some time of walking, you come across a wooden door, with a sign hangin on the front. The sign read, 'THE WORMS HEAD'. You think about how terrible a name it is as you open the door to reveal a tavern. It is mostly empty, save for a burly bartender behind the counter, and a mysterious figure sat at the bar."
    )
    print("")
    choice = input(
      "You need questions. And you need them now. Shoould you talk to the bartender or approach the mysterious figure?"
    )
    if choice == "approach the mysterious figure" or choice == "Approach the mysterious figure":
      print(
        "You approach the mysterious figure. He wears a trenchcoat and a fedora, which shields his face from you. You ask him where you are, to which he replys that he will only answer your questions, if defeat him in a duel. He then pulls out a sword of his own, with an air of mystery about it just like himself. You prepare to fight him."
      )
      if cupboard == "YES":
        print(
          "You pull out your mystical sword and in one swing slice his sword in half, the power of your sword clearly greater than your opponents. He immediately yields, and sits back at the bar with a defeated sigh. He beckons you to sit on the stool next to him."
        )
        beatenFigure()
      else:
        print(
          "You realise you have no weapon, and in a last minute attempt, you pull out your recently acquired dynamite. Before you can use it, however, the figure swings at you, colliding with the dynamite and detonating it. Safe to say 'The Worms Head' won't have another happy hour anytime soon."
        )
        print("This is the end of your journey. Better luck next time.")
    elif choice == "talk to the bartender" or choice == "Talk to the bartender":
      talkBartender()


def bedChoice(cupboard):
  print("")
  print("You walk over to the cliff and leanover, looking downwards.")
  print(
    "The clouds cover the area, and you cant see a thing"
  )
  print(
      "You stand up to leave, but trip on a small rock and fall through the clouds, only to realize it is a massive drop. You fall down down down into the depths of the world..."
    )
  holeOption(cupboard)


def cupboardChoice(cupboard):
  print("")
  print(
    "You walk over to the tree. Its very old. You see a small opening in the tree trunk"
  )
  print("")
  choice = input("will you put your hand in?")
  print("")
  if choice == "Yes" or choice == "yes":
    print(
      "You slide your hand inside and pull out an object covered in a blinding light. The blinding light is revealed to be a reflection of a mythical sword."
    )
    print("")
    print(
      "You pick up the sword and feel surge of energy flow into you. You slide it into your sheath, and the light fades."
    )
    cupboard = "YES"
    print("You walk back into the centre of the cliff.")
    return cupboard
  elif choice == "No" or choice == "no":
    print("You walk back into the centre of the cliff")
    print("")
    main(cupboard)


def main(cupboard):
  choice = ""
  print(
    "You are in atop a huge plateu. There is a tree to your left and the cliff to your right."
  )
  print("Go to tree")
  print("Or go to cliff")
  choice = input("where will you go?")
  print("")
  if (choice == "tree" or choice == "go to tree" or choice
      == "Tree" or choice == "Go to tree") and cupboard == "YES":
    print("You sense nothing of importance in this area")
    main(cupboard)
  elif choice == "cliff" or choice == "Cliff" or choice == "Go to cliff" or choice == "go to cliff":
    bedChoice(cupboard)
  elif choice == "tree" or choice == "go to tree" or choice == "Tree" or choice == "Go to tree":
    cupboard = cupboardChoice(cupboard)
    main(cupboard)

cupboard = "NO"
if __name__ == "__main__":
  main(cupboard)
