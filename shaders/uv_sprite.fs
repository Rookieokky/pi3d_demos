precision mediump float;

uniform sampler2D tex0;
uniform sampler2D tex1;
uniform sampler2D tex2;
uniform vec3 unib[4];

varying float texnum;

void main(void) {
  vec4 texc = vec4(0.0);
  if (texnum == 0.0) texc += texture2D(tex0, gl_PointCoord);
  if (texnum == 1.0) texc += texture2D(tex1, gl_PointCoord);
  if (texnum == 2.0) texc += texture2D(tex2, gl_PointCoord);
  //--------- alternatively use the non-obvious method below which might be quicker -------
  //texc += step(-0.5, texnum) * (1.0 - step(0.5, texnum)) * texture2D(tex0, gl_PointCoord);
  //texc += step(0.5, texnum) * (1.0 - step(1.5, texnum)) * texture2D(tex1, gl_PointCoord);
  //texc += step(1.5, texnum) * (1.0 - step(2.5, texnum)) * texture2D(tex2, gl_PointCoord);
  if (texc.a < unib[0][2]) discard; // ------ to allow rendering behind the transparent parts of this object
  gl_FragColor = texc;
}


