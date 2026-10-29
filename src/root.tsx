import React from 'react';
import {Composition} from 'remotion';
import {ProbabilityVideo} from './video';
export const Root: React.FC = () => <Composition id="ProbabilityV3" component={ProbabilityVideo} width={1920} height={1080} fps={30} durationInFrames={1800} />;
