# this is a state-based game that moves through a 3 dimensional position hierarchy until submission
# the hierarchy is defined by advantage (offense/defense) position (body orientation) and move (grab/block)
# the game starts in offense/standing/neutral/stand

PositionalHierarchy = [ 
	offense [
		standing [
			neutral[stand,crouch], 
			leftsleeve[stand,crouch], 
			rightsleeve[stand,crouch], 
			leftcollar[stand,crouch], 
			rightcollar[stand,crouch], 
			LsleeveRcollar[stand,crouch[start,step]],
			RsleeveLcollar[stand,crouch[start,step]],
			sleeveSleeve[stand,crouch], #to flyingTriangle#
			collarCollar[stand,crouch] #to CrossCollarChoke#
			],
		guard [
			neutral, 
			leftarm, #to armBar#
			rightsarm, #to armBar#
			leftcollar, #to CrossCollarChoke#
			rightcollar, #to CrossCollarChoke#
			LarmRcollar, #to Triangle#
			RarmLcollar, #to Triangle#
			PushLeft, 
			PushRight, 
			HeadGrab, #to Headlock#
			],
		halfGuard [
			neutral[right,left],
			sprawl,
			arm[right,left], #to keyLock#
			legOut[right,left],
			legUp[right,left],
			liftToBack
			],
		SideControl [
			neutral[right,left],
			wheelLock[right,left],
			sprawl[right,left],
			sitOut[right,left],
			reverseSitOut[right,left],
			],
		KneeOnBelly [
			neutral,
			leftArm[right,left], #to keyLock#
			rightArm[right,left], #to keyLock#
			legOver
			],
		NorthSouth [
			neutral,
			sprawl,
			liftToBack
			],
		Mount [
			leftArm, #to keyLock#
			rightArm, #to keyLock#
			leftcollar, #to CrossCollarChoke#
			rightcollar, #to CrossCollarChoke#
			LarmRcollar, #to sittingTriangle#
			RarmLcollar, #to sittingTriangle#
			],
		Turtle [
			leftArm,
			rightArm,
			LarmLhook, #to rearNakedChoke#
			LarmRhook, #to rearNakedChoke#
			RarmRhook, #to rearNakedChoke#
			RarmLhook, #to rearNakedChoke#
			],
		Back [
			leftArm,
			rightArm,
			LarmLhook, #to rearNakedChoke#
			LarmRhook, #to rearNakedChoke#
			RarmRhook, #to rearNakedChoke#
			RarmLhook, #to rearNakedChoke#
			]
		],
	defense [
		standing [ 
			leftsleeve,
			rightsleeve,
			leftcollar,
			rightcollar,
			pullGuard,
			],
		guard [
			neutral, 
			leftArmBlock,
			rightArmBlock,
			leftCollarBlock,
			rightCollarBlock,
			leftKneePush,
			rightKneePush,
			bothKneePush,
			],
		halfGuard [
			neutral[right,left],
			bridge[right,left],
			shrimp[right,left],
			armDefend[right,left], 
			],
		SideControl [
			neutral[right,left],
			bridge[right,left],
			shrimp[right,left],
			kneeIn[right,left],
			],
		KneeOnBelly [
			neutral[right,left],
			bridge[right,left],
			shrimp[right,left],
			roll[right,left]
			],
		NorthSouth [
			neutral,
			bridge,
			shrimp,
			roll,
			],
		Mount [
			neutral,
			bridge,
			shrimp,
			roll,
			],
		Turtle [
			neutral,
			leftarmGrab,
			rightarmGrab,
			roll
			],
		Back [
			neutral,
			leftarmGrab,
			rightarmGrab,
			roll
			],
		]
	]

init Position = PositionalHierarcy[offense][standing][neutral][stand]

if offense {
	if standing {
		if neutral {
			if stand{

			}
			if crouch{

			}} 
		if leftsleeve{
			 if stand{

			}
			if crouch{

			}}
		if rightsleeve{
			if stand{

			}
			if crouch{

			}} 
		if leftcollar{
			if stand{

			}
			if crouch{

			}}
		if rightcollar{
			if stand{

			}
			if crouch{

			}}
		if LsleeveRcollar{
			if stand{

			}
			if crouch{

			}}
		if RsleeveLcollar{
			if stand{

			}
			if crouch{

			}}
		if sleeveSleeve{
			if stand{

			}
			if crouch{

			}}
		if collarCollar{
			if stand{

			}
			if crouch{

			}}
			
		}

	}



