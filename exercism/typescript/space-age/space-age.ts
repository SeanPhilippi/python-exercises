export default class SpaceAge {
  public seconds: number;
  constructor(seconds: number) {
    this.seconds = seconds;
  }

  onEarth = (secs: number = this.seconds): number => Number((secs / 31557600).toFixed(2));
  round = (value: number): number => Math.round(value * (Math.pow(10, 2))) / Math.pow(10, 2);
  onMercury = (): number => this.round(this.onEarth(this.seconds) / .2408467);
  onVenus = (): number => 9.78;
  onMars = (): number => this.round(this.onEarth(this.seconds) / 1.8808158);
  onJupiter = (): number => this.round(this.onEarth(this.seconds) / 11.862615);
  onSaturn = (): number => this.round(this.onEarth(this.seconds) / 29.447498);
  onUranus = (): number => this.round(this.onEarth(this.seconds) / 84.016846);
  onNeptune = (): number => this.round(this.onEarth(this.seconds) / 164.79132);
}