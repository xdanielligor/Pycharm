
class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """Inicia o robô e define os componentes."""
        self.motor = wpilib.PWMVictorSPX(0)  # Motor na porta PWM 0
        self.joystick = wpilib.Joystick(0)   # Joystick na porta USB 0

    def teleopPeriodic(self):
        """Código executado repetidamente no modo teleoperado."""
        speed = self.joystick.getY()  # Lê o eixo Y do joystick (-1 a 1)
        self.motor.set(speed)  # Ajusta a velocidade do motor

if __name__ == "__main__":
    from robotpy import run
    run(MyRobot)
